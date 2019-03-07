import logging

from django.conf import settings
from django.core.management.base import BaseCommand
from twilio.rest import Client

from core.models import SMS

logger = logging.getLogger()


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        for sms in SMS.objects.filter(is_sent=False):
            try:
                client.messages.create(
                    body=sms.message, from_=settings.TWILIO_FROM_NUMBER, to=sms.number
                )
            except Exception as e:
                logger.error(e)
