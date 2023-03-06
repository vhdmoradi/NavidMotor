from django.contrib import admin

from .models import Agency


class AgencyAdmin(admin.ModelAdmin):
    autocomplete_fields = ["city", "province"]


admin.site.register(Agency, AgencyAdmin)
