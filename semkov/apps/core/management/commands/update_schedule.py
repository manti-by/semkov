import json
from collections import defaultdict

import requests

from bs4 import BeautifulSoup

from django.conf import settings
from django.core.management.base import BaseCommand

WEEK_DAYS = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")


class Command(BaseCommand):
    @staticmethod
    def convert_bus_days(days: list) -> dict:
        return {
            "mon": "пн" in days,
            "tue": "вт" in days,
            "wed": "ср" in days,
            "thu": "чт" in days,
            "fri": "пт" in days,
            "sat": "сб" in days,
            "sun": "вс" in days,
        }

    @staticmethod
    def clean_title(item: dict) -> str:
        return item["title"].replace("-", " - ").replace("_", " ").title()

    def get_bus_schedule(self) -> list:
        result = []
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
        }
        data = {
            "cityFrom": settings.BUS_API_POINT_FROM_NAME,
            "POINT_FROM": settings.BUS_API_POINT_FROM_ID,
            "cityTo": settings.BUS_API_POINT_TO_NAME,
            "POINT_TO": settings.BUS_API_POINT_TO_ID,
        }
        response = requests.post(settings.BUS_API_BASE_URL, data=data, headers=headers)
        if response.ok:
            for item in response.json():
                for stop in item["sub_shedule"]:
                    if stop["point"] == settings.BUS_API_POINT_FROM_NAME:
                        result.append(
                            {
                                "route": self.clean_title(item),
                                "route_number": item["number"],
                                "time": stop["arTime"],
                                "days": self.convert_bus_days(item["days"]),
                                "is_minibus": False,
                            }
                        )
        return result

    @staticmethod
    def get_minibus_schedule() -> list:
        result = []
        for link in settings.MINIBUS_ROUTES:
            response = requests.get(f"{settings.MINIBUS_BASE_URL}{link}")
            if response.ok:
                parser = BeautifulSoup(response.content, features="html5lib")
                schedule = defaultdict(lambda: {x: False for x in WEEK_DAYS})
                for timings, day in zip(
                    parser.find_all(class_="rowtime")[0].find_all("td"), WEEK_DAYS
                ):
                    for time in timings.find_all("li"):
                        schedule[time.text][day] = True
                for time, days in schedule.items():
                    route_number = (
                        parser.find(class_="breadcrumb")
                        .find_all("li")[5]
                        .find("a")
                        .text
                    )
                    result.append(
                        {
                            "route": parser.find(class_="now-route")
                            .find("h2")
                            .text.replace("—", "-"),
                            "route_number": f"1{route_number}",
                            "time": time.zfill(5),
                            "days": days,
                            "is_minibus": True,
                        }
                    )
        return result

    def handle(self, *args, **options):
        bus_schedule = self.get_bus_schedule()
        minibus_schedule = self.get_minibus_schedule()
        result = sorted(bus_schedule + minibus_schedule, key=lambda x: x["time"])
        with open(settings.SCHEDULE_FILE_PATH, "w") as f:
            f.write(json.dumps(result, indent=2, ensure_ascii=False))
