from django.shortcuts import render
from .models import Project, Skill

# Create your views here.


def index(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()

    for project in projects:
        project.technologies = project.technologies.split(",")
    context = {
      'projects': projects,
      'skills': skills
    }
    return render(request, 'home/index.html', context)
