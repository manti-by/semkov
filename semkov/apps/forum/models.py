from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page

from semkov.apps.core.mixins import AttachmentsMixin, MenuMixin


class ForumModel(MenuMixin, Page):
    text = RichTextField()

    content_panels = [*Page.content_panels, FieldPanel("text")]
    promote_panels = [*Page.promote_panels, *MenuMixin.promote_panels]

    class Meta:
        verbose_name = "Forum"
        verbose_name_plural = "Forums"


class ThreadModel(MenuMixin, AttachmentsMixin, Page):
    text = RichTextField()

    content_panels = [*Page.promote_panels, *AttachmentsMixin.content_panels, FieldPanel("text")]
    promote_panels = [*Page.promote_panels, *MenuMixin.promote_panels]

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"


class MessageModel(MenuMixin, AttachmentsMixin, Page):
    text = RichTextField()

    content_panels = [*Page.promote_panels, *AttachmentsMixin.content_panels, FieldPanel("text")]
    promote_panels = [*Page.promote_panels, *MenuMixin.promote_panels]

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
