from django.conf.urls import patterns, url
from site_details import views

urlpatterns = patterns(
    '',
    url(r'^about/', views.about, name='about'),
    url(r'^lab/', views.lab, name='lab'),
    url(r'^research/', views.research, name='research'),
)
