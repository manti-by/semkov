from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.blocks import ListBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page
from wagtail.templatetags import wagtailcore_tags


class ImagesMixin(Page):
    images = StreamField(
        [("images", ListBlock(ImageChooserBlock()))],
        blank=True,
        null=True,
        use_json_field=True,
    )

    content_panels = [FieldPanel("images")]

    class Meta:
        abstract = True


class AttachmentsMixin(Page):
    attachments = StreamField(
        [("attachments", ListBlock(DocumentChooserBlock()))],
        blank=True,
        null=True,
        use_json_field=True,
    )

    content_panels = [FieldPanel("attachments")]

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
