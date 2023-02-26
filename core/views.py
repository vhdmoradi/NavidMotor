from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib import messages
from django.core.serializers import serialize
import json

from .forms import ContactUsForm
from .models import SiteDataKeyValue
from salesnetwork.models import Agency


class HomePageView(ListView):
    """
    In this view we are fetching site data from database, in a function named get_context_data. In this function,
    we filter the model for objects that contains the word 'اصلی', therefore fetching data referring to the main page
    only. After that the context list is sent to the template, and there with a for loop and an if statement,
    each key, value set is chosen for the proper place.
    """

    model = SiteDataKeyValue
    template_name: str = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["home_page_data"] = self.model.objects.filter(key__icontains="اصلی")
        return context

    # just test:


class AboutPageView(ListView):
    """
    In this view we are fetching site data from database, in a function named get_context_data. In this function,
    we filter the model for objects that contains the word 'درباره', therefore fetching data referring to the about
    page only. After that the context list is sent to the template, and there with a for loop and an if statement,
    each key, value set is chosen for the proper place.
    """

    model = SiteDataKeyValue
    template_name: str = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPageView, self).get_context_data(**kwargs)
        context["about_page_data"] = self.model.objects.filter(key__icontains="درباره")
        return context


# my previous view, without form
# class ContactUsPageView(ListView):
#     """
#     In this view we are fetching site data from database, in a function named get_context_data. In this function,
#     we filter the model for objects that contains the word 'تماس', therefore fetching data referring to the about
#     page only. After that the context list is sent to the template, and there with a for loop and an if statement,
#     each key, value set is chosen for the proper place.
#     """
#
#     model = SiteDataKeyValue
#     template_name: str = "core/contact-us.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(ContactUsPageView, self).get_context_data(**kwargs)
#         context["contact_page_data"] = self.model.objects.filter(key__icontains="تماس")
#         return context


class ContactUsPageView(ListView):
    model = SiteDataKeyValue
    template_name: str = "core/contact-us.html"
    context_object_name = "contact_page_data"
    success_url = "/"

    def get_queryset(self):
        return SiteDataKeyValue.objects.filter(key__icontains="تماس")

    def get_context_data(self, **kwargs):
        form = ContactUsForm()
        context = super().get_context_data(**kwargs)
        if not kwargs.get("form"):
            context["form"] = form

        return context

    def post(self, request, **kwargs):
        data = request.POST
        self.object_list = self.get_queryset()
        form = ContactUsForm(data)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "پیام شما با موفقیت ارسال گردید. کارشناسان ما در صورت نیاز با شما تماس خواهند گرفت.",
            )
            return redirect("/contact-us/")
        form = ContactUsForm()
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


# class ContactUsSuccessView(TemplateView):
#     template_name: str = "core/contact_us_success.html"
