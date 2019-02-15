from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from app.mixins import ImagesMixin, ArticleMixin, MenuMixin


class PageModel(MenuMixin, ImagesMixin, ArticleMixin, Page):

    content_panels = Page.content_panels + \
        ArticleMixin.content_panels + \
        ImagesMixin.content_panels

    promote_panels = Page.promote_panels + \
        MenuMixin.promote_panels
