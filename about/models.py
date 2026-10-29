from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.


class About(models.Model):
    heading = models.CharField(max_length=150)
    my_image = CloudinaryField("image", blank=True)
    introduction = models.TextField()
    my_journey = models.TextField(blank=True)

    what_i_bring = models.TextField(blank=True)
    my_interests_passions = models.TextField(blank=True)

    looking_for = models.TextField(blank=True)
    contact_button_text = models.CharField(max_length=50, default="Hire Hana")
    LinkedIn_url = models.URLField(blank=True)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading


