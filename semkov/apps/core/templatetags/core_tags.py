from operator import itemgetter

from django import template
from django.conf import settings

from wagtail.models import Page


register = template.Library()


def get_ordered(page, is_homepage):
    result = []
    for current_page in page.get_children().live().in_menu():
        if is_homepage and not current_page.specific.is_homepage:
            continue

        children = get_ordered(current_page, is_homepage)
        if hasattr(current_page.specific, "menu_title"):
            title = current_page.specific.menu_title

            if is_homepage:
                title = current_page.specific.homepage_title

            result.append(
                {
                    "url": current_page.url,
                    "path": current_page.path,
                    "title": title,
                    "children": children,
                }
            )
    return sorted(result, key=itemgetter("path"))


@register.inclusion_tag("tags/main_menu.html")
def main_menu(show_index=False, is_homepage=False):
    return {
        "show_index": show_index,
        "menu_items": get_ordered(Page.objects.get(slug="index"), is_homepage),
    }


@register.inclusion_tag("tags/header.html", takes_context=True)
def header(context):
    return context


@register.simple_tag
def get_settings(value):
    return getattr(settings, value)
