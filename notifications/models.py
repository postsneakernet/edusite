from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField(max_length=130)
    publish = models.BooleanField(default=True)
    expiration = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
