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


class Skill(models.Model):
    icon = models.ImageField(upload_to="skills")
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)


def __str__(self):
    return self.name


class Meta:
    verbose_name = 'Skill'
    verbose_name_plural = 'Skills'
