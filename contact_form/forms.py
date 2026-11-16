from django import forms


ENQUIRY_CHOICES = [
    ("", "Please select an option"),
    ("job", "Junior Developer Opportunities"),
    ("freelance", "Freelance Project"),
    ("website", "Website Development"),
    ("collaboration", "Collaboration"),
    ("general", "General Enquiry"),
    ("other", "Other"),
]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    enquiry_type = forms.ChoiceField(choices=ENQUIRY_CHOICES)
    subject = forms.CharField(max_length=150, required=False)
    message = forms.CharField(widget=forms.Textarea)
