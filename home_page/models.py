from django.db import models

# Create your models here.


class Project(models.Model):
    image = models.ImageField(
        upload_to="projects")
    project_title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=250)
    github_url = models.URLField()
    live_url = models.URLField()


def __string__(self):
    return self.project_title


def add_project(self):
    project = {'project_title', 'project_description', 'technologies', 'github_link', 'live_link'}
    return project(self.project, self.description, self.technologies)

