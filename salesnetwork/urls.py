from django.urls import path


from .views import sales_network_page


urlpatterns = [
    path("", sales_network_page, name="sales_network"),
]
