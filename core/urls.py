from django.urls import path
from .views import (
    AboutPageView,
    HomePageView,
    ContactUsPageView,
    # ContactUsSuccessView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about-us/", AboutPageView.as_view(), name="about_us"),
    path("contact-us/", ContactUsPageView.as_view(), name="contact_us"),
]
