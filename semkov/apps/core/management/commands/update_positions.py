import json
import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

import requests
from bs4 import BeautifulSoup
from requests import RequestException
from wagtail.models import Page

from ...services.amon_ra import send_message


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    timeout = 60

    @staticmethod
    def clean_data(data) -> str:
        return data.text.replace("\xa0", " ").strip()

    @staticmethod
    def clean_schedule(item: str) -> list | None:
        result = []
        if not item:
            return
        schedule = item.split("\n")
        result.append(f"{schedule[0].title()} - {schedule[1]}")
        if len(schedule) > 3:
            result.append(f"{schedule[2].replace(':', '').title()} - {schedule[3]}")
        return result

    @staticmethod
    def clean_operations(item: str) -> list:
        return [x.capitalize() for x in item.replace("- ", "").replace(";", "").split("\n")]

    def get_positions(self) -> list:
        result = []
        response = requests.get(settings.POSITIONS_URL, timeout=self.timeout)
        if response.ok:
            parser = BeautifulSoup(response.content, features="html5lib")
            for index, row in enumerate(parser.find(class_="newscontainer-itemFullText").find_all("tr")):
                if not index:
                    continue
                cols = [self.clean_data(x) for x in row.find_all("td")]
                phone = cols[3][:9].replace(" ", "-")
                result.append(
                    {
                        "position": cols[1],
                        "full_name": cols[2].replace("\n", " "),
                        "phone": f"8 (017) {phone}",
                        "schedule": self.clean_schedule(cols[4]),
                        "operations": self.clean_operations(cols[5]),
                    }
                )
        logger.info(f"Imported {len(result)} positions")
        return result

    def handle(self, *args, **options):
        try:
            result = self.get_positions()
            with open(settings.POSITION_FILE_PATH, "w") as f:
                f.write(json.dumps(result, indent=2, ensure_ascii=False))
            Page.objects.filter(slug__in=(settings.POSITION_PAGE_SLUG, settings.CATEGORY_PAGE_SLUG)).update(
                last_published_at=timezone.now()
            )
        except RequestException as e:
            logger.error(e)
            send_message(_("Positions update error"), str(e))
