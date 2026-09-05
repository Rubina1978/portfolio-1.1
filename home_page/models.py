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
