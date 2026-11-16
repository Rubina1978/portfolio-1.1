from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail


def contact_form(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            enquiry_type = form.cleaned_data["enquiry_type"]
            message = form.cleaned_data["message"]
            send_mail(
                subject=f"Contact form: {enquiry_type}",
                message=f"""
                Name: {name}
                Email: {email}
                Enquiry type: {enquiry_type}

                Message:
                {message}
                """,
                from_email=None,
                recipient_list=["rubesovah@gmail.com"],
                fail_silently=False,
            )
            return render(
                request,
                "contact_form/contact_form.html",
                {
                    "form": form,
                    "submitted": True,
                    "name": name,
                    "email": email,
                    "enquiry_type": enquiry_type,
                    "message": message,
                },
            )

    return render(request, "contact_form/contact_form.html", {"form": form})
