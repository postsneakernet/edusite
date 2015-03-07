from django.db import models

def misc_dir(instance, filename):
    return '/'.join(['misc_pages', instance.slug, filename])

def file_dir(instance, filename):
    return '/'.join(['misc_pages', instance.misc_page.slug, filename])

class MiscPageQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class MiscPage(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    is_external_link = models.BooleanField(default=False)
    external_link = models.CharField(max_length=1000, null=True, blank=True)
    misc_file = models.FileField(upload_to=misc_dir, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    side = models.TextField(null=True, blank=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = MiscPageQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-modified']


class File(models.Model):
    file = models.FileField(upload_to=file_dir)
    misc_page = models.ForeignKey(MiscPage)
    added = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
