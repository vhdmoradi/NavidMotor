from django.db import models


from core.models import City, Province


class Agency(models.Model):
    English = "En"
    Persian = "Fa"
    Arabic = "Ar"
    LANG_CHOICE = [
        (English, "English"),
        (Persian, "Persian"),
        (Arabic, "Arabic"),
    ]
    language = models.CharField(
        max_length=2,
        choices=LANG_CHOICE,
        default=Persian,
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
    )
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    owner_name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )
    telephone = models.CharField(max_length=11, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    fax = models.CharField(max_length=11, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "agencies"

    def __str__(self):
        return self.title

    autocomplete_fields = ["city", "province"]
