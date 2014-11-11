from django.shortcuts import render
from site_details.models import Detail


def about(request):
    info = Detail.objects.all()
    context = {'about': info[0].about,
            'instructor_name': info[0].instructor_name,
            'modified': info[0].modified,
            'office': info[0].office,
            'email': info[0].email,
            'photo': info[0].photo,
            }
    
    return render(request, 'about.html', context)

def lab(request):
    info = Detail.objects.all()
    context = {'lab': info[0].lab,
            'lab_name': info[0].lab_name,
            'lab_room': info[0].lab_room,
            'lab_photo': info[0].lab_photo,
            'instructor_name': info[0].instructor_name,
            'modified': info[0].modified,
            }

    return render(request, 'lab.html', context)

def research(request):
    info = Detail.objects.all()
    context = {'research': info[0].research, 
            'research_photo': info[0].research_photo,
            'instructor_name': info[0].instructor_name,
            'instructor_title': info[0].instructor_title,
            'modified': info[0].modified,
            'education': info[0].education,
            'employment': info[0].employment,
            'other_resume': info[0].other_resume,
            }

    return render(request, 'research.html', context)
