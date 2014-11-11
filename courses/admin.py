from django.contrib import admin
from django.utils.html import format_html_join
from django.utils.safestring import mark_safe
from django_markdown.admin import MarkdownModelAdmin

from . import models


class CourseAdmin(MarkdownModelAdmin):
    list_display = ("title", "created", "modified")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['-modified']


class FileInline(admin.TabularInline):
    model = models.File


class ModuleAdmin(MarkdownModelAdmin):
    readonly_fields = ('file_use',)

    def file_use(self, instance):
        msg = "/media/courses/" + instance.course.slug + "/modules/" + instance.slug + "/file"
        return msg

    inlines = [FileInline, ]
    list_display = ("title","topic", "course", "created", "publish")
    fields = (('title', 'course'),
        ('prefix', 'slug'), 
        'topic', 'module_pdf', 'file_use', 'body', 'activity', 'publish')
    prepopulated_fields = {"slug": ("prefix", "title",)}
    ordering = ['course']


class AssignmentAdmin(MarkdownModelAdmin):
    list_display = ("title", "course", "created", "publish")
    ordering = ['-created']


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Module, ModuleAdmin)
admin.site.register(models.Assignment, AssignmentAdmin)
