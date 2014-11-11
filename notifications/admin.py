from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin

class NotificationAdmin(MarkdownModelAdmin):
    list_display = ("title","course", "created","expiration", "publish")
    #ordering = ['course']


admin.site.register(models.Notification, NotificationAdmin)
