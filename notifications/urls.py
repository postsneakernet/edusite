from django.conf.urls import patterns, url
from notifications import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='notifications'),
)
