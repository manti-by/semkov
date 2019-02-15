from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.blocks import ListBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class ImagesMixin(Page):

    images = StreamField([
        ('images', ListBlock(ImageChooserBlock()))
    ], blank=True, null=True)

    content_panels = [
        StreamFieldPanel('images'),
    ]

    class Meta:
        abstract = True


class AttachmentsMixin(Page):

    attachments = StreamField([
        ('attachments', ListBlock(DocumentChooserBlock()))
    ], blank=True, null=True)

    content_panels = [
        StreamFieldPanel('attachments'),
    ]

    class Meta:
        abstract = True


class ArticleMixin(Page):

    excerpt = RichTextField()
    text = RichTextField()
    source = models.URLField()

    content_panels = [
        FieldPanel('excerpt'),
        FieldPanel('text'),
        FieldPanel('source'),
    ]

    class Meta:
        abstract = True


class MenuMixin(Page):

    menu_title = models.CharField(max_length=32, blank=True)

    promote_panels = [
        FieldPanel('menu_title'),
    ]

    class Meta:
        abstract = True
