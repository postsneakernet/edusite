from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin

from misc_pages import models

class FileInline(admin.TabularInline):
    model = models.File

class MiscPageAdmin(MarkdownModelAdmin):
    readonly_fields = ('file_use',)

    def file_use(self, instance):
        if instance.slug:
            islug = instance.slug
        else:
            islug = "misc-page-slug"

        return "/media/lessons/" + islug + "/filename"

    inline = [FileInline, ]
    list_display = ("title", "created", "is_external_link", "publish")
    fieldsets = (
        (None, {
            'fields': (('title', 'slug'),)
        }),
        ('External link options', {
            'classes': ('collapse',),
            'fields': ('is_external_link', 'external_link', ('misc_file',),)
        }),
        ('Misc page content', {
            'fields': ('body', 'side', 'publish',)
        }),
    )

    prepopulated_fields = {"slug": ("title",)}
    order = ['title']

admin.site.register(models.MiscPage, MiscPageAdmin)
