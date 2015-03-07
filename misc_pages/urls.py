from django.conf.urls import patterns, url
from misc_pages import views

urlpatterns = patterns(
    '',
    url(r'^$', views.MiscPageIndex.as_view(), name="misc_index"),
    url(r'^(?P<misc_page_slug>\S+)$', views.misc_page_detail, name="misc_detail"),
)
