from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel

from app.mixins import AttachmentsMixin


class ForumModel(Page):

    text = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]

    parent_page_types = ['home.HomepageModel']
    allowed_subpage_models = ['forum.ThreadModel']


class ThreadModel(AttachmentsMixin, Page):

    text = RichTextField()

    content_panels = Page.content_panels + \
        AttachmentsMixin.content_panels + \
        [
            FieldPanel('text'),
        ]

    parent_page_types = ['forum.ForumModel']
    allowed_subpage_models = ['forum.MessageModel']


class MessageModel(AttachmentsMixin, Page):

    text = RichTextField()

    content_panels = Page.content_panels + \
        AttachmentsMixin.content_panels + \
        [
            FieldPanel('text'),
        ]

    parent_page_types = ['forum.ThreadModel']
    allowed_subpage_models = []
