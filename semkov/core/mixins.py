from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.api import APIField
from wagtail.core.blocks import ListBlock
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page
from wagtail.core.templatetags import wagtailcore_tags
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock


class ImagesMixin(Page):

    images = StreamField(
        [("images", ListBlock(ImageChooserBlock()))], blank=True, null=True
    )

    content_panels = [StreamFieldPanel("images")]

    class Meta:
        abstract = True


class AttachmentsMixin(Page):

    attachments = StreamField(
        [("attachments", ListBlock(DocumentChooserBlock()))], blank=True, null=True
    )

    content_panels = [StreamFieldPanel("attachments")]

    class Meta:
        abstract = True


class ArticleMixin(Page):

    excerpt = RichTextField()
    text = RichTextField()
    source_title = models.TextField(blank=True)
    source = models.URLField(blank=True)

    content_panels = [
        FieldPanel("excerpt"),
        FieldPanel("text"),
        FieldPanel("source_title"),
        FieldPanel("source"),
    ]

    def rendered_text(self):
        return wagtailcore_tags.richtext(self.text)

    api_fields = [APIField("rendered_text")]

    class Meta:
        abstract = True


class MenuMixin(Page):

    is_homepage = models.BooleanField(default=False)
    homepage_title = models.CharField(max_length=32, blank=True)
    menu_title = models.CharField(max_length=32, blank=True)

    promote_panels = [
        FieldPanel("is_homepage"),
        FieldPanel("homepage_title"),
        FieldPanel("menu_title"),
    ]

    class Meta:
        abstract = True
