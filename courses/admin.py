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
        msg = "/~zalewski/media/courses/" + instance.course.slug + "/modules/" + instance.slug + "/file"
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
    fields = (('title', 'semester',), ('course', 'slug',), 'due_date',
            'assignment_pdf', 'misc_file', 'body', 'publish')

    prepopulated_fields = {"slug": ("semester", "title",)}
    ordering = ['-created']


class ProjectAdmin(MarkdownModelAdmin):
    #def get_form(self, request, obj=None, **kwargs):
    #    self.exclude = []
    #    if request.user.is_superuser:
    #        self.exclude.append('due_date')
    #    return super(ProjectAdmin, self).get_form(request, obj, **kwargs)

    fieldsets = (
        (None, {
            'fields': (('title', 'semester', 'course',), ('group', 'slug',),)
        }),
        ('Options for project requirement submission', {
            'classes': ('collapse',),
            'fields': ('requirement', 'due_date',)
        }),
        ('Project content', {
            'fields': ('project_pdf', 'misc_file', 'body', ('publish', 'archive'))
        }),
    )

    list_display = ("title", "course", "semester", "created", "requirement", 
            "publish", "archive")
    prepopulated_fields = {"slug": ("semester", "title",)}
    ordering = ['course']


admin.site.register(models.Course, CourseAdmin)
admin.site.register(models.Module, ModuleAdmin)
admin.site.register(models.Assignment, AssignmentAdmin)
admin.site.register(models.Project, ProjectAdmin)
