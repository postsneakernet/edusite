from django.conf.urls import patterns, url
from courses import views

urlpatterns = patterns(
    'courses',
    url(r'^(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/get/$', 
            'views.get_files', name="get_files"),
    #url(r'^(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/pdf/$', 
            #'views.get_pdf', name="get_pdf"),
    url(r'^(?P<course_slug>[-\w]+)/modules/(?P<module_slug>[-\w]+)/$', 
            'views.module_detail', name="module_detail"),
    url(r'^(?P<course_slug>[-\w]+)/modules/$', 'views.modules', name="modules"),
    url(r'^(?P<course_slug>[-\w]+)/assignments/$', 'views.assignments', 
        name="assignments"),
    url(r'^(?P<course_slug>[-\w]+)/projects/$', 'views.projects', name="projects"),
    url(r'^(?P<course_slug>[-\w]+)/syllabus/$', 'views.syllabus', name="syllabus"),
    url(r'^(?P<course_slug>[-\w]+)/notifications/$', 'views.notifications', 
            name="course_notifications"),
    url(r'^(?P<course_slug>[-\w]+)/posts/(?P<post_slug>[-\w]+)/$',
            'views.course_post', name="course_post"),
    url(r'^(?P<course_slug>[-\w]+)/$', 'views.course_home', name="course_home"),
    url(r'^$', views.CourseIndex.as_view(), name="course_index"),
)
