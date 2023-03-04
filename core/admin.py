from django.contrib import admin

from .models import SiteDataKeyValue, City, Province, ContactUsFormModel


admin.site.register(SiteDataKeyValue)
admin.site.register(City)
admin.site.register(Province)
admin.site.register(ContactUsFormModel)
