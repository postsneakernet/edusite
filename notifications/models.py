from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
    publish = models.BooleanField(default=True)
    expiration = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
