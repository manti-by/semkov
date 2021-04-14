import logging

from email.mime.image import MIMEImage

from django.conf import settings
from django.contrib.staticfiles import finders
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string

from semkov.apps.core.models import Email

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    @staticmethod
    def logo_data():
        with open(finders.find("img/appicon/128x128.png"), "rb") as f:
            logo_data = f.read()
        logo = MIMEImage(logo_data)
        logo.add_header("Content-ID", "<logo>")
        return logo

    def handle(self, *args, **options):
        for email in Email.objects.filter(is_sent=False):
            try:
                text_content = render_to_string("emails/email.txt", {"email": email})
                html_content = render_to_string("emails/email.html", {"email": email})

                message = EmailMultiAlternatives(
                    email.subject,
                    body=text_content,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=(settings.DEFAULT_TO_EMAIL,),
                )
                message.mixed_subtype = "related"
                message.attach_alternative(html_content, "text/html")
                message.attach(self.logo_data())
                message.send(fail_silently=False)

                email.is_sent = True
                email.save()
            except Exception as e:
                logger.error(e)
