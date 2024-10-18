import json

from django import template
from django.conf import settings


register = template.Library()


@register.inclusion_tag("tags/schedule.html")
def schedule():
    headers = ["Время", "№№", "Маршрут", "Дни недели"]
    with open(settings.ARRIVAL_FILE_PATH) as file:
        arrival = json.loads(file.read())
    with open(settings.DEPARTURE_FILE_PATH) as file:
        departure = json.loads(file.read())
    return {
        "headers": headers,
        "days": range(1, 8),
        "arrival": arrival.values(),
        "departure": departure.values(),
    }


@register.inclusion_tag("tags/position.html")
def position():
    headers = ["Должность", "ФИО", "Телефон", "Время приема", "Рассматриваемые вопросы"]
    with open(settings.POSITION_FILE_PATH) as file:
        items = json.loads(file.read())
    return {"headers": headers, "items": items}
