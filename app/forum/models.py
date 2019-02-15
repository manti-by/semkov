from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from app.mixins import AttachmentsMixin, MenuMixin


class ForumModel(MenuMixin, Page):

    text = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]

    promote_panels = Page.promote_panels + \
        MenuMixin.promote_panels


class ThreadModel(MenuMixin, AttachmentsMixin, Page):

    text = RichTextField()

    content_panels = Page.content_panels + \
        AttachmentsMixin.content_panels + \
        [
            FieldPanel('text'),
        ]

    promote_panels = Page.promote_panels + \
        MenuMixin.promote_panels


class MessageModel(MenuMixin, AttachmentsMixin, Page):

    text = RichTextField()

    content_panels = Page.content_panels + \
        AttachmentsMixin.content_panels + \
        [
            FieldPanel('text'),
        ]

    promote_panels = Page.promote_panels + \
        MenuMixin.promote_panels
