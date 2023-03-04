from django.contrib import admin
from django.db.models.functions import Lower

from .models import (
    MainModel,
    Usage,
    SubUsage,
    PumpType,
    Product,
    HeadFlowDataset,
)


class MainModelAdmin(admin.ModelAdmin):
    fields = (
        "model_name_fa",
        "model_name_en",
        "model_image",
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.last_updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()


class UsageAdmin(admin.ModelAdmin):
    fields = (
        "usage_name_fa",
        "usage_name_en",
        "usage_image",
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.last_updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()


class SubUsageAdmin(admin.ModelAdmin):
    list_display = (
        "sub_usage_name_fa",
        "usage",
    )
    fields = (
        "sub_usage_name_fa",
        "sub_usage_name_en",
        "usage",
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.last_updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()


class PumpTypeAdmin(admin.ModelAdmin):
    list_display = (
        "type_name",
        "main_model",
    )
    fields = (
        "type_name",
        "description_fa",
        "description_en",
        "main_model",
    )

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.last_updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()


class HeadFlowDatasetInline(admin.TabularInline):
    model = HeadFlowDataset
    extra = 0
    ordering = ("-flow",)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "pump_name",
        "main_model",
        "pump_type",
    )
    search_fields = (
        "pump_name",
        "main_model__model_name_fa",
        "usage__usage_name_fa",
        "pump_type__type_name",
    )
    fields = (
        "main_model",
        "usage",
        "sub_usage",
        "pump_type",
        "pump_name",
        "pump_image",
        "NPSH_diagram_image",
        "power_diagram_image",
        "max_head",
        "max_flow",
        "motor_ph",
        "motor_rpm",
        "pump_technical_datasheet_fa",
        "pump_technical_datasheet_en",
    )
    inlines = [HeadFlowDatasetInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        return super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save()
        for instance in instances:
            instance.user = request.user
            instance.save()


class HeadFlowDatasetAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "head",
        "flow",
    )
    fields = (
        "product",
        "head",
        "flow",
    )
    autocomplete_fields = ["product"]

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.last_updated_by = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            instance.user = request.user
            instance.save()

    def get_ordering(self, request):
        return [Lower("product__pump_name"), "flow"]


admin.site.register(MainModel, MainModelAdmin)
admin.site.register(Usage, UsageAdmin)
admin.site.register(PumpType, PumpTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(SubUsage, SubUsageAdmin)
admin.site.register(HeadFlowDataset, HeadFlowDatasetAdmin)
