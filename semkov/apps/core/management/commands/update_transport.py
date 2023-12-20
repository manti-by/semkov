import json
import logging
from collections import defaultdict, OrderedDict

import requests
from django.conf import settings
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    base_url = "https://transport-by.app/api"
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
        "Content-Type": "application/json",
    }
    timeout = 60
    stop_ids = ("25948176", "114793481")
    minibus_stop_id = "114793481"

    def get_routes(self) -> list | None:
        result = []
        for stop_id in self.stop_ids:
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
                                "is_minibus": self.minibus_stop_id == stop_id,
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

    def handle(self, *args, **options):
        result = {}
        for route in self.get_routes():
            for time, days in self.get_route_schedule(route).items():
                result[time] = route.copy()
                result[time]["time"] = time
                result[time]["days"] = list(map(int, days))

        with open(settings.SCHEDULE_FILE_PATH, "w") as f:
            result = dict(sorted(result.items(), key=lambda x: x[0]))
            f.write(json.dumps(result, indent=2, ensure_ascii=False))
        logger.info(f"Imported {len(result)} routes")
