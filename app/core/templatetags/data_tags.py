import csv

from django import template

register = template.Library()


def compile_days(row):
    return {
        'Monday': row[3] == '1',
        'Tuesday': row[4] == '1',
        'Wednesday': row[5] == '1',
        'Thursday': row[6] == '1',
        'Friday': row[7] == '1',
        'Saturday': row[8] == '1',
        'Sunday': row[9] == '1',
    }


@register.inclusion_tag("tags/route_list.html")
def route_list(document):
    items = []
    with open(document.file.path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            items.append({
                'number': row[0],
                'route': row[1],
                'time': row[2],
                'days': compile_days(row),
            })
    return {
        "items": items,
    }
