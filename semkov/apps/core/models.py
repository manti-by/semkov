from django.db import models


class Email(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    meta = models.TextField(blank=True, null=True)
    is_sent = models.BooleanField(blank=True, default=False)
    created = models.DateTimeField(auto_now_add=True)
