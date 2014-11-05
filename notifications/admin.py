from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin

class NotificationAdmin(MarkdownModelAdmin):
    list_display = ("title", "created")


admin.site.register(models.Notification, NotificationAdmin)
