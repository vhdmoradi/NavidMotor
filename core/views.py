from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import ContactUsForm

# from django.forms.models import model_to_dict


from .models import SiteDataKeyValue


class HomePageView(ListView):
    """
    In this view we are fetching site data from database, in a function named get_context_data. In this function, we filter the model for objects that contains the word 'اصلی', therefore fetching data referring to the main page only. After that the context list is sent to the template, and there with a for loop and an if statement, each key, value set is chosen for the proper place.
    """

    model = SiteDataKeyValue
    template_name: str = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["home_page_data"] = self.model.objects.filter(key__icontains="اصلی")
        return context


class AboutPageView(ListView):
    """
    In this view we are fetching site data from database, in a function named get_context_data. In this function, we filter the model for objects that contains the word 'درباره', therefore fetching data referring to the about page only. After that the context list is sent to the template, and there with a for loop and an if statement, each key, value set is chosen for the proper place.
    """

    model = SiteDataKeyValue
    template_name: str = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context["about_page_data"] = self.model.objects.filter(key__icontains="درباره")
        return context


class ContactUsPageView(ListView):
    """
    In this view we are fetching site data from database, in a function named get_context_data. In this function, we filter the model for objects that contains the word 'تماس', therefore fetching data referring to the about page only. After that the context list is sent to the template, and there with a for loop and an if statement, each key, value set is chosen for the proper place.
    """

    model = SiteDataKeyValue
    template_name: str = "core/contact-us.html"

    def get_context_data(self, **kwargs):
        context = super(ContactUsPageView, self).get_context_data(**kwargs)
        context["contact_page_data"] = self.model.objects.filter(key__icontains="تماس")
        return context


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = "پیام ارسالی از فرم تماس با ما"
            body = {
                "first_name": form.changed_data["first_name"],
                "last_name": form.changed_data["last_name"],
                "email": form.changed_data["email_address"],
                "message": form.changed_data["message"],
            }

            message = "\n".join(body.values())

            try:
                send_mail(
                    subject,
                    message,
                    "vahid.moradi001@gmail.com",
                    ["vahid.moradi001@gmail.com"],
                )
            except BadHeaderError:
                return HttpResponse("Invalid header found.")

            return redirect(reverse("contact_us"))
    form = ContactUsForm()
    return render(request, "core/contact-us.html", {"form": form})
