from django.shortcuts import render

from .models import Project, Skill


def index(request):
    projects = Project.objects.all()
    for project in projects:
        project.technologies = project.technologies.split(',')

    skills_by_category = {
        'Frontend': Skill.objects.filter(
            category='Frontend').order_by('order'),
        'Backend': Skill.objects.filter(
            category='Backend').order_by('order'),
        'Database': Skill.objects.filter(
            category='Database').order_by('order'),
        'Tools/Services': Skill.objects.filter(
            category='Tools/Services').order_by('order'),
    }

    context = {
        'projects': projects,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'home/index.html', context)
