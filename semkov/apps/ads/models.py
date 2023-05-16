from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField

from semkov.apps.core.mixins import ImagesMixin, MenuMixin


class AdsModel(MenuMixin, ImagesMixin, Page):
    text = RichTextField()

    content_panels = (
        [FieldPanel("text")] + Page.content_panels + ImagesMixin.content_panels
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Adverts"
