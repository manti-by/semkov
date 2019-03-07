from django.contrib import admin

from core.models import Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'subject', 'is_sent', 'created')
