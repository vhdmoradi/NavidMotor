from django.db import models
from django.utils import timezone


# from salesnetwork.models import Provinces, Cities


class SiteDataKeyValue(models.Model):
    # //TODO add name field
    # //TODO add fields value_fa, value_en and value_ar
    key = models.CharField(
        max_length=200, verbose_name="نام متن مورد نظر", unique=True
    )
    value = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.key


class Province(models.Model):
    province_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    # //TODO connected dropdown
    city_id = models.BigAutoField(primary_key=True)
    province_id = models.ForeignKey(
        Province, on_delete=models.SET_NULL, default=None, null=True
    )
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "cities"

    def __str__(self):
        return self.name


# This model is for contact form
class ContactUsFormModel(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    province = models.ForeignKey(
        Province, on_delete=models.DO_NOTHING, default=None, null=True
    )
    # // TODO add phone number field
    # phone_number = models.IntegerField(max_length=11)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=250, blank=False, null=False)
    message_body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
