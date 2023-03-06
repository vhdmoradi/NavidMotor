from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import (
    Product,
    Usage,
    SubUsage,
    MainModel,
    PumpType,
    HeadFlowDataset,
)


def get_common_queryset():
    usage_queryset = Usage.objects.all()
    sub_usage_queryset = SubUsage.objects.all()
    main_model_queryset = MainModel.objects.all()
    pump_type_queryset = PumpType.objects.all()
    queryset_dictionary = {
        "usage_queryset": usage_queryset,
        "sub_usage_queryset": sub_usage_queryset,
        "main_model_queryset": main_model_queryset,
        "pump_type_queryset": pump_type_queryset,
    }
    return queryset_dictionary


def get_head_flow_list(product_list_queryset):
    head_flow_list_main = []
    for product in product_list_queryset:
        head_flow_list = HeadFlowDataset.objects.filter(
            product_id=product.id
        ).order_by("flow")
        head_flow_list_main.append(head_flow_list)
    return head_flow_list_main


def return_filtered_products(head_flow_list_main, head, flow):
    product_list = []
    for head_flow_list in head_flow_list_main:
        for i in range(head_flow_list.count() - 1):
            if head_flow_list[i].flow <= flow <= head_flow_list[i + 1].flow:
                if head * 0.9 <= head_flow_list[i + 1].head <= head * 1.3:
                    if head_flow_list[i].product_id not in product_list:
                        product_list.append(head_flow_list[i].product_id)

    return product_list


def products_usage_main(request):
    queryset_dictionary = get_common_queryset()
    context = queryset_dictionary
    return render(request, "products/products_usage_main.html", context)


def products_single_usage_list(request, pk):
    product_list_queryset = Product.objects.filter(usage=pk).order_by(
        "pump_name"
    )
    if request.method == "POST":
        flow = float(request.POST["flow"])
        head = float(request.POST["head"])
        head_flow_list_main = get_head_flow_list(product_list_queryset)
        product_list = return_filtered_products(
            head_flow_list_main, head, flow
        )
        product_list_queryset = Product.objects.filter(id__in=product_list)

    page = request.GET.get("page", 1)
    paginator = Paginator(product_list_queryset, 10)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    usage_title_fa = Usage.objects.get(id=pk).usage_name_fa
    usage_title_en = Usage.objects.get(id=pk).usage_name_en
    context_of_view = {
        "product_list": product_list,
        "usage_title_fa": usage_title_fa,
        "usage_title_en": usage_title_en,
    }
    queryset_dictionary = get_common_queryset()
    context = {
        **context_of_view,
        **queryset_dictionary,
        "message": "hello",
    }
    return render(request, "products/products_single_usage_list.html", context)


def products_sub_usage_list(request, pk):
    product_list_queryset = Product.objects.filter(sub_usage=pk).order_by(
        "pump_name"
    )
    if request.method == "POST":
        flow = float(request.POST["flow"])
        head = float(request.POST["head"])
        head_flow_list_main = get_head_flow_list(product_list_queryset)
        product_list = return_filtered_products(
            head_flow_list_main, head, flow
        )
        product_list_queryset = Product.objects.filter(id__in=product_list)
    page = request.GET.get("page", 1)
    paginator = Paginator(product_list_queryset, 10)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    sub_usage_title_fa = SubUsage.objects.get(id=pk).sub_usage_name_fa
    sub_usage_title_en = SubUsage.objects.get(id=pk).sub_usage_name_en
    context_of_view = {
        "product_list": product_list,
        "sub_usage_title_fa": sub_usage_title_fa,
        "sub_usage_title_en": sub_usage_title_en,
    }
    queryset_dictionary = get_common_queryset()
    context = {
        **context_of_view,
        **queryset_dictionary,
    }
    return render(
        request, "products/products_single_sub_usage_list.html", context
    )


def products_model_main(request):
    queryset_dictionary = get_common_queryset()
    context = queryset_dictionary
    return render(request, "products/products_model_main.html", context)


def products_single_model_list(request, pk):
    product_list_queryset = Product.objects.filter(main_model=pk).order_by(
        "pump_name"
    )
    if request.method == "POST":
        flow = float(request.POST["flow"])
        head = float(request.POST["head"])
        head_flow_list_main = get_head_flow_list(product_list_queryset)
        product_list = return_filtered_products(
            head_flow_list_main, head, flow
        )
        product_list_queryset = Product.objects.filter(id__in=product_list)
    page = request.GET.get("page", 1)
    paginator = Paginator(product_list_queryset, 10)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    model_title_fa = MainModel.objects.get(id=pk).model_name_fa
    model_title_en = MainModel.objects.get(id=pk).model_name_en
    context_of_view = {
        "product_list": product_list,
        "model_title_fa": model_title_fa,
        "model_title_en": model_title_en,
    }
    queryset_dictionary = get_common_queryset()
    context = {
        **context_of_view,
        **queryset_dictionary,
    }
    return render(request, "products/products_single_model_list.html", context)


def products_single_type_list(request, pk):
    product_list_queryset = Product.objects.filter(pump_type=pk).order_by(
        "pump_name"
    )
    if request.method == "POST":
        flow = float(request.POST["flow"])
        head = float(request.POST["head"])
        head_flow_list_main = get_head_flow_list(product_list_queryset)
        product_list = return_filtered_products(
            head_flow_list_main, head, flow
        )
        product_list_queryset = Product.objects.filter(id__in=product_list)
    page = request.GET.get("page", 1)
    paginator = Paginator(product_list_queryset, 10)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)
    pump_type_title_fa = PumpType.objects.get(id=pk).type_name
    pump_type_title_en = PumpType.objects.get(id=pk).type_name
    context_of_view = {
        "product_list": product_list,
        "pump_type_title_fa": pump_type_title_fa,
        "pump_type_title_en": pump_type_title_en,
    }
    queryset_dictionary = get_common_queryset()
    context = {
        **context_of_view,
        **queryset_dictionary,
    }
    return render(request, "products/products_single_type_list.html", context)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    head_flow_dataset = HeadFlowDataset.objects.filter(
        product=product
    ).order_by("flow")
    context_of_view = {
        "product": product,
        "head_flow_dataset_x": [],
        "head_flow_dataset_y": [],
    }
    for head_flow in head_flow_dataset:
        context_of_view["head_flow_dataset_x"].append(head_flow.flow)
        context_of_view["head_flow_dataset_y"].append(head_flow.head)
    queryset_dictionary = get_common_queryset()
    context = {
        **context_of_view,
        **queryset_dictionary,
    }
    return render(request, "products/product_detail.html", context)
