from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from core.mixins import ImagesMixin, MenuMixin


class AdsModel(MenuMixin, ImagesMixin, Page):

    text = RichTextField()

    content_panels = (
        [FieldPanel("text")] + Page.content_panels + ImagesMixin.content_panels
    )

    promote_panels = Page.promote_panels + MenuMixin.promote_panels
