from django.shortcuts import render
from .models import Project

# Create your views here.


def index(request):
    projects = Project.objects.all()

    for project in projects:
        project.technologies = project.technologies.split(",")
    context = {
      'projects': projects
    }
    return render(request, 'home/index.html', context)
