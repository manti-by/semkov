from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.blocks import PageChooserBlock
from wagtail.core.fields import RichTextField
from wagtail.documents.blocks import DocumentChooserBlock

from app.home.models import CategoryModel


class ForumModel(CategoryModel):

    text = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]


class ThreadModel(ForumModel):

    text = RichTextField()
    attachments = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='treads_attachments'
    )

    content_panels = Page.content_panels + [
        FieldPanel('text'),
        DocumentChooserBlock('attachments')
    ]


class MessageModel(ThreadModel):

    text = RichTextField()
    attachments = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='messages_attachments'
    )

    content_panels = Page.content_panels + [
        FieldPanel('text'),
        DocumentChooserBlock('attachments')
    ]
