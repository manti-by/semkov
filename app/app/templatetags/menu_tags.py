from operator import itemgetter

from django import template
from wagtail.core.models import Page

register = template.Library()


def get_ordered(page):
    result = []
    for current_page in page.get_children().live().in_menu():
        children = get_ordered(current_page)
        if hasattr(current_page.specific, 'menu_title'):
            result.append({
                'url': current_page.url,
                'path': current_page.path,
                'title': current_page.specific.menu_title,
                'children': children
            })
    return sorted(result, key=itemgetter('path'))


@register.inclusion_tag('tags/main_menu.html')
def main_menu():
    return {
        'menu_items': get_ordered(Page.objects.get(slug='index'))
    }
