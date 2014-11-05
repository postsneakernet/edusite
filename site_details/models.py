from django.db import models
from django.core.urlresolvers import reverse


class DetailQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Detail(models.Model):
    title = models.CharField(max_length=200, verbose_name="site title")
    instructor_name = models.CharField(max_length=200)
    instructor_title = models.CharField(max_length=200)
    about = models.TextField()
    lab = models.TextField()
    research = models.TextField()
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    objects = DetailQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("about_detail")
