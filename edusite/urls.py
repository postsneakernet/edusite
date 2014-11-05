from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^detail/', include('site_details.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^', include('posts.urls')),
)

handler404 = 'edusite.views.error404'
