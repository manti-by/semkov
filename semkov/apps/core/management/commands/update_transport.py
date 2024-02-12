from __future__ import annotations

import json
import logging
from collections import defaultdict
from typing import TYPE_CHECKING

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from pathlib import PosixPath


class Command(BaseCommand):
    base_url = "https://transport-by.app/api"
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Content-Type": "application/json",
    }
    timeout = 60

    bus_type = 3
    arrival_stop_ids = ("25948176", "114793481")
    departure_stop_ids = ("25699328",)

    def get_routes(self, stop_ids: tuple) -> list[dict] | None:
        result = []
        for stop_id in stop_ids:
            response = requests.post(
                f"{self.base_url}/GetStopRouts",
                data=json.dumps({"StopId": stop_id, "Types": None}),
                headers=self.headers,
                timeout=self.timeout,
            )
            if response.ok:
                for item in map(
                    json.loads,
                    filter(lambda x: x, response.content.decode().split("\n")),
                ):
                    if data := item.get("result"):
                        result.append(
                            {
                                "stop_id": stop_id,
                                "route_id": data.get("RouteId"),
                                "number": data.get("Number"),
                                "route": f"{data.get('StartStopName')} - {data.get('FinishStopName')}",
                                "is_minibus": data.get("Type") == self.bus_type,
                            }
                        )
        return result

    def get_route_schedule(self, route: dict) -> dict:
        result = defaultdict(list)
        response = requests.post(
            f"{self.base_url}/GetSchedule",
            data=json.dumps({"StopId": route["stop_id"], "RouteId": route["route_id"]}),
            headers=self.headers,
            timeout=self.timeout,
        )
        if response.ok:
            for item in response.json().get("Items", []):
                result[f"{item['Hour']}:{item['Minutes']}"].append(item["Days"])

        sorted_values = {key: sorted(list(set(value))) for key, value in result.items()}
        return dict(sorted(sorted_values.items(), key=lambda x: x[0]))

    def get_schedule(self, stop_ids: tuple, file_path: PosixPath):
        result = {}
        for route in self.get_routes(stop_ids):
            for time, days in self.get_route_schedule(route).items():
                result[time] = route.copy()
                result[time]["time"] = time
                result[time]["days"] = list(map(int, days))
        with open(file_path, "w") as f:
            result = dict(sorted(result.items(), key=lambda x: x[0]))
            f.write(json.dumps(result, indent=2, ensure_ascii=False))
        logger.info(f"Imported {len(result)} routes to file {file_path}")

    def handle(self, *args, **options):
        self.get_schedule(self.arrival_stop_ids, settings.ARRIVAL_FILE_PATH)
        self.get_schedule(self.departure_stop_ids, settings.DEPARTURE_FILE_PATH)
