from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin


class DetailAdmin(MarkdownModelAdmin):
    list_display = ("title", "modified")


admin.site.register(models.Detail, DetailAdmin)
