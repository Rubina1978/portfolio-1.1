from django.shortcuts import render
from .models import About, keyFacts

# Create your views here.


def about_me(request):
    about_me = About.objects.first()
    key_facts = keyFacts.objects.all()

    highlighted_sentences = []

    if about_me and about_me.highlighted_sentences:
        sentences = about_me.highlighted_sentences.split("|")

        for sentence in sentences:
            sentence = sentence.strip()

            if sentence:
                highlighted_sentences.append(sentence)

    return render(
        request, "about/about.html", {
            "about_me": about_me,
            "key_facts": key_facts,
            "highlighted_sentences": highlighted_sentences
        })
