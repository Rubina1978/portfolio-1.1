from django.shortcuts import render
from .models import About

# Create your views here.


def about_me(request):
    about_me = About.objects.first()

    what_i_bring_cards = []

    if about_me and about_me.what_i_bring:
        cards = about_me.what_i_bring.splitlines()

        for card in cards:
            parts = card.split("|", 1)

            if len(parts) == 2:
                what_i_bring_cards.append(
                    {"title": parts[0].strip(),
                        "description": parts[1].strip()})

    return render(
        request, "about/about.html", {
            "about_me": about_me,
            "what_i_bring_cards": what_i_bring_cards

        })
