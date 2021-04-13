import csv

from django import template

register = template.Library()


def get_route_data(row):
    return (
        row[:3],
        {
            "Monday": row[3] == "1",
            "Tuesday": row[4] == "1",
            "Wednesday": row[5] == "1",
            "Thursday": row[6] == "1",
            "Friday": row[7] == "1",
            "Saturday": row[8] == "1",
            "Sunday": row[9] == "1",
        },
    )


@register.inclusion_tag("tags/document_table.html")
def document_table(document, classes=None):
    items = []
    with open(document.file.path, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data = row
            days = None
            if "route" in classes:
                data, days = get_route_data(row)
            items.append({"data": data, "days": days})
    return {"items": items, "classes": classes}
