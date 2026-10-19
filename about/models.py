from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class About(models.Model):
    heading = models.CharField(max_length=150)
    my_image = CloudinaryField("image", blank=True)
    introduction = models.TextField()

    who_i_am = models.TextField()
    what_i_bring = models.TextField()
    my_interests_passions = models.TextField()

    looking_for = models.TextField()
    contact_button_text = models.CharField(max_length=50, default="Hire Hana")
    LinkedIn_url = models.URLField(blank=True)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading


class keyFacts (models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.title
