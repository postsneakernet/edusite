from django.views import generic
from django.utils import timezone

from . import models
from notifications.models import Notification
from site_details.models import Detail


class PostIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PostIndex, self).get_context_data(**kwargs)
        context['about'] = Detail.objects.all()
        #context['notifications'] = Notification.objects.all()
        context['notifications'] = Notification.objects.filter(
                            expiration__gte=timezone.now()
                                    ).order_by('-created')
        return context


class PostDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        list = Detail.objects.all()
        context['about'] = list
        return context
