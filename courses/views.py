from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.servers.basehttp import FileWrapper
from django.views import generic
from django.utils import timezone

import os, tempfile, zipfile

from courses.models import Course, Module, Assignment, File, Project
from posts.models import Entry, Tag
from notifications.models import Notification
from site_details.models import Detail


class CourseIndex(generic.ListView):
    template_name = 'courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CourseIndex, self).get_context_data(**kwargs)
        context['about'] = Detail.objects.all()
        context['modified'] = Course.objects.order_by('-modified')

        return context


def syllabus(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)

    return render(request, 'syllabus.html', {'course': course})


def modules(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    modules = Module.objects.published().filter(course__slug=course_slug)

    latest_module = modules.order_by('-created')[:1]

    return render(request, 'modules.html', 
            {'course': course, 'modules': modules,'latest_module': latest_module,})


def module_detail(request, course_slug, module_slug):
    course = get_object_or_404(Course, slug=course_slug)
    module = get_object_or_404(Module, slug=module_slug)
    files = File.objects.filter(module__slug=module_slug)

    return render(request, 'module_detail.html', {'course': course, 
        'files': files, 'module': module})


'''
def get_pdf(request, course_slug, module_slug):
    fname = module_slug + ".pdf"
    httpf = "attachmet; filename=" + fname
'''


def get_files(request, course_slug, module_slug):
    f = File.objects.filter(module__slug=module_slug)
    fname = module_slug + ".zip"
    httpf = "attachment; filename=" + fname
    source_path = os.path.dirname(f[0].file.path)
    target_path = os.path.dirname(source_path)
    target_file = os.path.join(target_path, fname)
    relroot = os.path.abspath(os.path.join(source_path, os.pardir))

    with zipfile.ZipFile(target_file, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_path):
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename):
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)

    wrapper = FileWrapper(open(target_file, 'rb'))
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Length'] = os.path.getsize(target_file)
    response['Content-Disposition'] = httpf

    return response


def assignments(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    assignments = Assignment.objects.published().filter(course__slug=course_slug)
    latest_assignment = assignments.order_by('-created')[:1]

    return render(request, 'assignments.html', {'course': course, 
        'assignments': assignments, 'latest_assignment': latest_assignment})


def projects(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    p = Project.objects.all().filter(course__slug=course_slug)
    projects = p.students()
    requirements = p.requirements().order_by('-created')
    archives = p.archived()
    latest_project = requirements.order_by('-created')[:1]

    return render(request, 'projects.html', {'course': course, 
        'projects': projects, 'latest_project': latest_project,
        'requirements': requirements, 'archives': archives,
        })


def course_home(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    notifications = Notification.objects.published().filter(course__slug=course_slug)
    post_list = Entry.objects.published().filter(course__slug=course_slug)

    if len(post_list) > 2:
        is_paginated = True
    else:
        is_paginated = False

    paginator = Paginator(post_list, 2)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'course_home.html',
            {'course': course, 'posts': posts, 
                'is_paginated': is_paginated, 'notifications': notifications,})


def course_post(request, course_slug, post_slug):
    course = get_object_or_404(Course, slug=course_slug)
    post = get_object_or_404(Entry, slug=post_slug)
    tags = Tag.objects.all()

    return render(request, 'course_post.html',
            {'course': course, 'post': post, 'tags': tags})


def tag_index(request, tag_slug):
    posts = Entry.objects.published().filter(tags__slug=tag_slug)
    tags = Tag.objects.all()

    return render(request, 'tags.html',
            {'search_tag': tag_slug, 'tags': tags, 'posts': posts})


def notifications(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    notifications = Notification.objects.published().filter(course__slug=course_slug)
    posts = Entry.objects.published().filter(course__slug=course_slug)

    return render(request, 'course_notifications.html', 
            {'course': course, 'notifications': notifications, 'posts': posts})
