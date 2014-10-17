from django.shortcuts import render

def error404(request):
    return render(request, '404.html')
