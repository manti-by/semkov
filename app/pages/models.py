from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.core.fields import RichTextField

from core.mixins import ImagesMixin, ArticleMixin, MenuMixin


class PageModel(MenuMixin, ImagesMixin, ArticleMixin, Page):

    content_panels = (
        Page.content_panels + ArticleMixin.content_panels + ImagesMixin.content_panels
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels


class RoutePageModel(MenuMixin, ImagesMixin, ArticleMixin, Page):

    file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = (
        [DocumentChooserPanel("file")]
        + Page.content_panels
        + ImagesMixin.content_panels
        + ArticleMixin.content_panels
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels
