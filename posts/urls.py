from django.conf.urls import patterns, url
from . import views, feed

urlpatterns = patterns(
    '',
    url(r'^feed/$', feed.LatestPosts(), name="feed"),
    url(r'^$', views.PostIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', views.PostDetail.as_view(), name="entry_detail"),
)
