from django.db import models
from django.utils import timezone

from courses.models import Course

class NotificationQuerySet(models.QuerySet):
    def published(self):
        return self.filter(expiration__gt=timezone.now(), publish=True)


class Notification(models.Model):
    title = models.CharField(max_length=50)
    course = models.ForeignKey(Course, null=True, blank=True)
    body = models.TextField(max_length=200)
    expiration = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)

    objects = NotificationQuerySet.as_manager()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
