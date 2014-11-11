from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from posts.models import Entry, Tag
from notifications.models import Notification
from site_details.models import Detail


class PostIndex(generic.ListView):
    queryset = Entry.objects.published().filter(course__isnull=True)
    template_name = "home.html"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(PostIndex, self).get_context_data(**kwargs)
        context['about'] = Detail.objects.all()
        context['notifications'] = Notification.objects.published().filter(
                course__isnull=True)

        return context


class PostDetail(generic.DetailView):
    model = Entry
    template_name = "post.html"

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['about'] = Detail.objects.all()
        context['tags'] = Tag.objects.all()
        #context['tags'] = Entry.objects.published().filter(course__isnull=True)

        return context


def tag_index(request, tag_slug):
    posts = Entry.objects.published().filter(tags__slug=tag_slug)
    tags = Tag.objects.all()

    return render(request, 'tags.html',
            {'search_tag': tag_slug, 'tags': tags, 'posts': posts})
