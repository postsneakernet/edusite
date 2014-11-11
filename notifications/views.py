from django.shortcuts import render
from django.views import generic

from notifications.models import Notification
from posts.models import Entry


class OldIndexView(generic.ListView):
    template_name = 'notifications.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        return Notification.objects.published().filter(course__isnull=True)


class IndexView(generic.ListView):
    queryset = Notification.objects.published().filter(course__isnull=True)
    template_name = 'notifications.html'
    context_object_name = 'notifications'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['posts'] = Entry.objects.published().filter(course__isnull=True)

        return context
