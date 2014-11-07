from django.shortcuts import render
from django.views import generic
from notifications.models import Notification
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'notifications.html'
    context_object_name = 'notifcations'
    queryset = Notification.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['notifications'] = Notification.objects.all()
        return context

    #def get_queryset(self):
    #return Notification.objects.all()



#def index(request):
    #for item in Notification.objects.all():
    #list = Notification.objects.all()
    #context = {'notifications': list}
    #return render(request, 'notifications.html', context)
