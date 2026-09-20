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


def skills_view(request):
    frontend_skills = Skill.object.filter(category="frontend") 
    backend_skills = Skill.object.filter(category="backend")
    database = Skill.object.filter(category="database")
    tools = Skill.object.filter(category="tools/services")

    context = {
      'frontend_skills': frontend_skills,
      'backend_skills': backend_skills,
      'database': database,
      'tools': tools
    }
    return render(request, 'home/index.html', context)
