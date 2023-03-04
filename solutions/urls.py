from django.urls import path


from .views import (
    solution_main,
    solution_product_list,
    solution_head_flow_filter,
)

urlpatterns = [
    path("", solution_main, name="solution_main"),
    path(
        "product-list/",
        solution_product_list,
        name="solution_product_list",
    ),
    path(
        "product-list/head-flow-filter/",
        solution_head_flow_filter,
        name="solution_head_flow_filter",
    ),
]
