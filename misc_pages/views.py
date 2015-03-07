from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from misc_pages.models import MiscPage, File

class MiscPageIndex(generic.ListView):
    template_name = 'misc.html'
    context_object_name = 'misc_pages'

    def get_queryset(self):
        return MiscPage.objects.published


def misc_page_detail(request, misc_page_slug):
    misc_page = get_object_or_404(MiscPage, slug=misc_page_slug)

    return render(request, 'misc_detail.html', {'misc_page': misc_page})
