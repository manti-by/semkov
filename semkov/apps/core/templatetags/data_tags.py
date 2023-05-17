import json

from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag("tags/schedule.html")
def schedule():
    headers = ["Время", "№№", "Маршрут", "Дни недели"]
    with open(settings.SCHEDULE_FILE_PATH, mode="r") as file:
        items = json.loads(file.read())
    return {"headers": headers, "items": items}


@register.inclusion_tag("tags/position.html")
def position():
    headers = ["Должность", "ФИО", "Телефон", "Время приема", "Рассматриваемые вопросы"]
    with open(settings.POSITION_FILE_PATH, mode="r") as file:
        items = json.loads(file.read())
    return {"headers": headers, "items": items}
