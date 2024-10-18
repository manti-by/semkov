from django.db import models

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page

from semkov.apps.core.mixins import ArticleMixin, ImagesMixin, MenuMixin


class PageTag(TaggedItemBase):
    content_object = ParentalKey("pages.PageModel", related_name="page_tags")


class PageModel(MenuMixin, ImagesMixin, ArticleMixin, Page):
    map = models.TextField(blank=True)

    tags = ClusterTaggableManager(through="pages.PageTag", blank=True)

    content_panels = [
        FieldPanel("map"),
        FieldPanel("tags"),
        *Page.content_panels,
        *ArticleMixin.content_panels,
        *ImagesMixin.content_panels,
    ]
    promote_panels = [*Page.promote_panels, *MenuMixin.promote_panels]

    def tag_slugs(self):
        return self.tags.values_list("slug", flat=True)

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
