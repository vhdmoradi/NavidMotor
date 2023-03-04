from django.urls import path


from .views import (
    products_usage_main,
    product_detail,
    products_single_usage_list,
    products_sub_usage_list,
    products_model_main,
    products_single_model_list,
    products_single_type_list,
)


urlpatterns = [
    path("application/", products_usage_main, name="products_usage_main"),
    path("model/", products_model_main, name="products_model_main"),
    path("<str:pk>/", product_detail, name="product_detail"),
    path(
        "application/single-application/<str:pk>",
        products_single_usage_list,
        name="products_single_usage_list",
    ),
    path(
        "application/single-application/sub-application/<str:pk>",
        products_sub_usage_list,
        name="products_sub_usage_list",
    ),
    path(
        "model/single-model/<str:pk>",
        products_single_model_list,
        name="products_single_model_list",
    ),
    path(
        "model/single-model/pump-type/<str:pk>",
        products_single_type_list,
        name="products_single_type_list",
    ),
]
