from django.conf.urls import patterns, url
from searches import views

urlpatterns = patterns(
    '',
    url(r'^$', views.search, name="search"),
)
