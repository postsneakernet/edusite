from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
from django.db.models import Q
from courses.models import Module, Project, Assignment, Course
from posts.models import Entry
from notifications.models import Notification
from misc_pages.models import MiscPage

import re

def normalize_query(query_string,
        findterms=re.compile(r'"([^"])"|(\S+)').findall,
        normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in individual keywords, and removing spaces
        and grouping quoted words together.
    '''

    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns query that is a combination of Q objects
        Searches keywords within a model
    '''

    query = None # Query to search for every search term

    terms = normalize_query(query_string)

    for term in terms:
        or_query = None # Query to search for a given term in each field

        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q

        if query is None:
            query = or_query
        else:
            query = query & or_query

    return query


def search(request):
    query_string = ''
    module_entries = None
    post_entries = None
    notification_entries = None
    project_entries = None
    assignment_entries = None
    course_entries = None
    misc_entries = None

    if('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['title', 'body',])
        ce_query = get_query(query_string, ['title', 'syllabus',])

        misc_entries = MiscPage.objects.filter(entry_query).order_by('-created')
        module_entries = Module.objects.filter(entry_query).order_by('-created')
        post_entries = Entry.objects.filter(entry_query).order_by('-created')
        notification_entries = Notification.objects.filter(entry_query).order_by('-created')
        project_entries = Project.objects.filter(entry_query).order_by('-created')
        assignment_entries = Assignment.objects.filter(entry_query).order_by('-created')
        course_entries = Course.objects.filter(ce_query).order_by('-created')

    return render_to_response('search.html',
            {'query_string': query_string,
             'module_entries': module_entries,
             'project_entries': project_entries,
             'assignment_entries': assignment_entries,
             'course_entries': course_entries,
             'notification_entries': notification_entries,
             'misc_entries': misc_entries,
             'post_entries': post_entries},
             context_instance=RequestContext(request))
