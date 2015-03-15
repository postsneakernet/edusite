from django.conf.urls import patterns, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^$', views.PostIndex.as_view(), name="index"),
    url(r'^tags/(?P<tag_slug>\S+)/$', views.tag_index, name="tag_index"),
    url(r'^posts/(?P<slug>\S+)$', views.PostDetail.as_view(), name="entry_detail"),
)
