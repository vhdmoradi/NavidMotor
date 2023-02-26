import uuid

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from core.models import SiteDataKeyValue
from products.models import Usage, MainModel, SubUsage, PumpType, Product
from products.views import get_head_flow_list, return_filtered_products


def get_common_queryset():
    usage_queryset = Usage.objects.all()
    main_model_queryset = MainModel.objects.all()

    # to produce a dictionary with each Usage object as key and its sub_usages as a list for its value
    sub_usage_list_with_usage = {}
    sub_usage_list = []
    for usage in Usage.objects.all():
        for element in list(SubUsage.objects.filter(usage=usage)):
            sub_usage_list.append(
                [str(element.id), str(element.sub_usage_name_fa)]
            )
            sub_usage_list_with_usage[str(usage.id)] = sub_usage_list
        sub_usage_list = []
    # to produce a dictionary with each MainModel object as key and its pump_types as a list for its value
    pump_type_list_with_main_model = {}
    pump_type_list = []
    for main_model in MainModel.objects.all():
        for element in list(PumpType.objects.filter(main_model=main_model)):
            pump_type_list.append([str(element.id), str(element)])
            pump_type_list_with_main_model[str(main_model.id)] = pump_type_list
        pump_type_list = []
    queryset_dictionary = {
        "usage_queryset": usage_queryset,
        "main_model_queryset": main_model_queryset,
        "sub_usage_list_with_usage": sub_usage_list_with_usage,
        "pump_type_list_with_main_model": pump_type_list_with_main_model,
    }
    return queryset_dictionary


def solution_main(request):
    site_data_query = SiteDataKeyValue.objects.filter(key__icontains="راهکار")
    queryset_dictionary = get_common_queryset()
    print(queryset_dictionary)
    page_context = {
        "site_data_query": site_data_query,
    }
    context = {
        **queryset_dictionary,
        **page_context,
    }
    return render(request, "solutions/solution_main.html", context)


def solution_product_list(request):
    product_list_queryset = Product.objects.all()
    sub_usage_list = []
    pump_type_list = []
    usage_model_select = None
    usage_select = None
    sub_usage_select = None
    model_select = None
    pump_type_select = None
    if request.method == "POST":
        if "usage_model_select" in request.POST:
            usage_model_select = request.POST["usage_model_select"]
            if request.POST["usage_select"] != "----":
                usage_select = request.POST["usage_select"]
                product_list_queryset = Product.objects.filter(
                    usage__id=usage_select
                )
                sub_usage_list = SubUsage.objects.filter(
                    usage__id=usage_select
                )
                if request.POST["sub_usage_select"] != "all_sub_usages":
                    sub_usage_select = request.POST["sub_usage_select"]
                    product_list_queryset = Product.objects.filter(
                        sub_usage__id=sub_usage_select
                    )
            elif request.POST["model_select"] != "----":
                model_select = request.POST["model_select"]
                product_list_queryset = Product.objects.filter(
                    main_model__id=model_select
                )
                pump_type_list = PumpType.objects.filter(
                    main_model__id=model_select
                )
                if request.POST["pump_type_select"] != "all_pump_types":
                    pump_type_select = request.POST["pump_type_select"]
                    product_list_queryset = Product.objects.filter(
                        pump_type__id=pump_type_select
                    )
        if "head" in request.POST and "flow" in request.POST:
            try:
                flow = float(request.POST["flow"])
                head = float(request.POST["head"])
                head_flow_list_main = get_head_flow_list(product_list_queryset)
                product_list = return_filtered_products(
                    head_flow_list_main, head, flow
                )
                product_list_queryset = Product.objects.filter(
                    id__in=product_list
                )
            except ValueError:
                flow = None
                head = None
    page = request.GET.get("page", 1)
    paginator = Paginator(product_list_queryset, 10)
    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)

    queryset_dictionary = get_common_queryset()
    page_context = {
        "product_list": product_list_queryset,
        "usage_model_select": usage_model_select,
        "usage_select": usage_select,
        "sub_usage_select": sub_usage_select,
        "model_select": model_select,
        "pump_type_select": pump_type_select,
        "sub_usage_queryset": sub_usage_list,
        "pump_type_queryset": pump_type_list,
    }
    context = {
        **queryset_dictionary,
        **page_context,
    }
    return render(request, "solutions/second_stage_select.html", context)


def solution_head_flow_filter(request):
    pass
