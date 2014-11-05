from django.shortcuts import render
from site_details.models import Detail


def about(request):
    list = Detail.objects.all()
    about = list[0].about
    instructor_name = list[0].instructor_name
    context = {'about': about, 'instructor_name': instructor_name}
    return render(request, 'about.html', context)

def lab(request):
    list = Detail.objects.all()
    lab = list[0].lab
    instructor_name = list[0].instructor_name
    context = {'lab': lab, 'instructor_name': instructor_name}
    return render(request, 'lab.html', context)

def research(request):
    list = Detail.objects.all()
    research = list[0].research
    instructor_name = list[0].instructor_name
    instructor_title = list [0].instructor_title
    context = {'research': research, 
            'instructor_name': instructor_name,
            'instructor_title': instructor_title,
            }
    return render(request, 'research.html', context)
