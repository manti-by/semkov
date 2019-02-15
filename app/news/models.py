from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from app.home.models import CategoryModel


class NewsModel(CategoryModel):

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='news_images'
    )

    excerpt = RichTextField()
    text = RichTextField()
    source = models.URLField()

    content_panels = Page.content_panels + [
        ImageChooserPanel('image'),
        FieldPanel('excerpt'),
        FieldPanel('text'),
        FieldPanel('source'),
    ]
