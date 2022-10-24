from django.db import models


# class SiteData(models.Model):
#     data_set_name = models.CharField(
#         max_length=200, blank=False, null=False, default="نام مجموعه داده"
#     )
#     main_page_english_info = models.TextField(
#         verbose_name="مقدمه انگلیسی", blank=True, null=True
#     )
#     main_page_persian_info = models.TextField(
#         verbose_name="مقدمه فارسی", blank=True, null=True
#     )
#     about_page_pumpiran_info = models.TextField(
#         verbose_name="متن معرفی گروه پمپ ایران", blank=True, null=True
#     )
#     about_page_navid_motor_info = models.TextField(
#         verbose_name="متن معرفی شرکت نوید موتور", blank=True, null=True
#     )
#     about_us_why_navid_1 = models.TextField(
#         verbose_name="متن تبلیغاتی کارت تیپ و مدل", blank=True, null=True
#     )
#     about_us_why_navid_2 = models.TextField(
#         verbose_name="متن تبلیغاتی کارت خدمات پس از فروش", blank=True, null=True
#     )
#     about_us_why_navid_3 = models.TextField(
#         verbose_name="متن تبلیغاتی کارت مواد اولیه با کیفیت", blank=True, null=True
#     )

#     def __str__(self) -> str:
#         return self.data_set_name


class SiteDataKeyValue(models.Model):
    key = models.CharField(max_length=200, verbose_name="نام متن مورد نظر", unique=True)
    value = models.TextField(verbose_name="متن")

    def __str__(self):
        return self.key


# This model is for contact form
class ContactUsForm(models.Model):
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    # //TODO add province list to the form
    # province = ???
    # // TODO add phone number field
    # phone_number = models.IntegerField(max_length=11)
    email = models.EmailField(blank=False, null=False)
    subject = models.CharField(max_length=250, blank=False, null=False)
    message_body = models.TextField()

    def __str__(self):
        return self.subject
