from django.conf.urls import patterns, url
from notifications import views

urlpatterns = patterns(
    '',
    url(r'^index/', views.index, name='index'),
)
