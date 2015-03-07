from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^hi/', include('hello.urls')),
    url(r'^courses/', include('courses.urls')),
    url(r'^detail/', include('site_details.urls')),
    url(r'^notifications/', include('notifications.urls')),
    url(r'^misc/', include('misc_pages.urls')),
    url(r'^search/', include('searches.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/', include("django_markdown.urls")),
    url(r'^', include('posts.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

handler404 = 'edusite.views.error404'
