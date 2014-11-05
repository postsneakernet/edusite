from django.shortcuts import render
from notifications.models import Notification

def index(request):
    list = Notification.objects.all()
    title = list[0].title
    body = list[0].body
    context = {'title': title, 'body': body}
    return render(request, 'notifications.html', context)
