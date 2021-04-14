from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

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
        ImageChooserPanel("image"),
        ImageChooserPanel("background"),
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
