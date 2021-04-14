from django.contrib import admin

from semkov.apps.core.models import Email, SMS


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ("name", "contact", "subject", "is_sent", "created")


@admin.register(SMS)
class SMSAdmin(admin.ModelAdmin):
    list_display = ("number", "message", "is_sent", "created")
