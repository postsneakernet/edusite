from django.views import generic
from . import models

class PostIndex(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "home.html"
    paginate_by = 2


class PostDetail(generic.DetailView):
    model = models.Entry
    template_name = "post.html"
