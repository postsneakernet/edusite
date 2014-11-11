from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from . import models


class EntryAdmin(MarkdownModelAdmin):
    list_display = ("title", "course", "created", "publish")
    ordering = ['course']
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
