from django.shortcuts import render
import json

from .models import Agency
from core.models import SiteDataKeyValue


def sales_network_page(request):
    data_query = SiteDataKeyValue.objects.filter(key__icontains="شبکه")

    context = {
        "agency_list": [],
        "sales_network_page_data": data_query,
    }
    temp_dict = {}
    agency_queryset = Agency.objects.all()

    for agency in agency_queryset:
        temp_dict["id"] = agency.id
        temp_dict["language"] = agency.language
        temp_dict["province"] = agency.province.name
        temp_dict["city"] = agency.city.name
        temp_dict["title"] = agency.title
        temp_dict["owner_name"] = agency.owner_name
        temp_dict["address"] = agency.address
        temp_dict["telephone"] = agency.telephone
        temp_dict["mobile"] = agency.mobile
        temp_dict["fax"] = agency.fax
        temp_dict["latitude"] = float(agency.latitude)
        temp_dict["longitude"] = float(agency.longitude)
        context["agency_list"].append(temp_dict)
        temp_dict = {}

    return render(request, "salesnetwork/sales_network.html", context)
