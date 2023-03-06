from django.contrib import admin

from .models import SiteDataKeyValue, City, Province, ContactUsFormModel


class CityAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name"]


class ProvinceAdmin(admin.ModelAdmin):
    ordering = ["name"]
    search_fields = ["name"]


admin.site.register(SiteDataKeyValue)
admin.site.register(City, CityAdmin)
admin.site.register(Province, ProvinceAdmin)
admin.site.register(ContactUsFormModel)
