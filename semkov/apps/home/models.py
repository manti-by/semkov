from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

from semkov.apps.core.mixins import MenuMixin


class HomepageModel(MenuMixin, Page):
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="homepage_images",
    )
    background = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="homepage_backgrounds",
    )

    content_panels = Page.content_panels + [
        FieldPanel("image"),
        FieldPanel("background"),
    ]

    promote_panels = Page.promote_panels + MenuMixin.promote_panels

    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepages"


class CategoryModel(MenuMixin, Page):
    text = RichTextField()

    content_panels = Page.content_panels + [FieldPanel("text")]

    promote_panels = Page.promote_panels + MenuMixin.promote_panels

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
