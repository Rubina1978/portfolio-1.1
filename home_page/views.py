from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Project

# Create your views here.


def index(request):
    projects = Project.objects.all()
    context = {
      'projects': projects
    }
    return render(request, 'home/index.html', context)
