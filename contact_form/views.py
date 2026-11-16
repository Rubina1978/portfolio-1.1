from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages


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
                recipient_list=["hrubesova2712@gmail.com"],
                fail_silently=False,

            )
            messages.success(
                request,
                "Thank you for your enqiry! \
                Your message has been sent successfully.")
            return redirect("contact")
        else:
            messages.error(
                request,
                "There has been an issue submitting you message.\
                 Please check if all fields are valid and try again.")
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

    return render(request, "contact_form/contact_form.html", {"form": form})
