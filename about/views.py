from django.shortcuts import render
from .models import About, keyFacts

# Create your views here.


def about_me(request):
    about_me = About.objects.first()
    key_facts = keyFacts.objects.all()

    return render(
        request, "about/about.html", {
            "about_me": about_me,
            "key_facts": key_facts,
        })
