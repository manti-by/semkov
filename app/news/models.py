from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from app.mixins import ImagesMixin, ArticleMixin


class NewsModel(ImagesMixin, ArticleMixin, Page):

    content_panels = Page.content_panels + \
        ArticleMixin.content_panels + \
        ImagesMixin.content_panels

    parent_page_types = ['home.CategoryModel']
    allowed_subpage_models = []
