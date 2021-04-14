from django.db import models

from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from semkov.apps.core.mixins import ImagesMixin, ArticleMixin, MenuMixin


class PageTag(TaggedItemBase):

    content_object = ParentalKey("pages.PageModel", related_name="page_tags")


class PageModel(MenuMixin, ImagesMixin, ArticleMixin, Page):

    document = models.ForeignKey(
        "wagtaildocs.Document",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    map = models.TextField(blank=True)

    tags = ClusterTaggableManager(through="pages.PageTag", blank=True)

    content_panels = (
        [DocumentChooserPanel("document"), FieldPanel("map"), FieldPanel("tags")]
        + Page.content_panels
        + ArticleMixin.content_panels
        + ImagesMixin.content_panels
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels

    def tag_slugs(self):
        return self.tags.values_list("slug", flat=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
