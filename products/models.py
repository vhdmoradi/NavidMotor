import uuid

from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
import os


# this function is for generating a unique name for each image that is being uploaded.
def path_and_rename_image(instance, filename):
    upload_to = "images/"
    ext = filename.split(".")[-1]
    # getting the image name
    if instance.id:
        filename = "{}.{}".format(
            instance.id,
            ext,
        )
    else:
        filename = "{}.{}".format(
            uuid.uuid4().hex,
            ext,
        )

    return os.path.join(upload_to, filename)


# this function is for generating a unique name for each document that is being uploaded.
def path_and_rename_file(instance, filename):
    upload_to = "docs/"
    ext = filename.split(".")[-1]
    # getting the image name
    if instance.id:
        filename = "{}.{}".format(
            instance.id,
            ext,
        )
    else:
        filename = "{}.{}".format(
            uuid.uuid4().hex,
            ext,
        )

    return os.path.join(upload_to, filename)


class MainModel(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    model_name_fa = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام فارسی مدل",
        unique=True,
    )
    model_name_en = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام انگلیسی مدل",
        unique=True,
    )
    model_image = models.ImageField(
        upload_to=path_and_rename_image,
        help_text="تصویر مدل الکتروپمپ",
        verbose_name="تصویر مدل الکتروپمپ",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="main_model_created_user",
    )
    last_updated_at = models.DateTimeField(
        auto_now=True,
    )
    last_updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="main_model_updated_user",
    )

    def __str__(self):
        return self.model_name_fa


class Usage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    usage_name_fa = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام فارسی کاربرد",
        unique=True,
    )
    usage_name_en = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام انگلیسی کاربرد",
        unique=True,
    )
    usage_image = models.ImageField(
        upload_to=path_and_rename_image,
        help_text="تصویر کاربرد",
        verbose_name="تصویر کاربرد",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usage_created_user",
    )
    last_updated_at = models.DateTimeField(
        auto_now=True,
    )
    last_updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usage_updated_user",
    )

    def __str__(self):
        return self.usage_name_fa


class SubUsage(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    sub_usage_name_fa = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام فارسی کاربرد جزئی",
    )
    sub_usage_name_en = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام انگلیسی کاربرد جزئی",
    )
    usage = models.ForeignKey(
        Usage,
        on_delete=models.CASCADE,
        verbose_name="کاربرد اصلی",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sub_usage_created_user",
    )
    last_updated_at = models.DateTimeField(
        auto_now=True,
    )
    last_updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sub_usage_updated_user",
    )

    def __str__(self):
        return (
            self.sub_usage_name_fa + " از کاربرد " + self.usage.usage_name_fa
        )


class PumpType(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    type_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام تیپ",
    )
    description_fa = models.TextField(
        verbose_name="مشخصات فنی تیپ به فارسی",
    )
    description_en = models.TextField(
        verbose_name="مشخصات فنی تیپ به انگلیسی",
    )
    main_model = models.ForeignKey(
        MainModel,
        on_delete=models.CASCADE,
        verbose_name="مدل اصلی",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pump_type_created_user",
    )
    last_updated_at = models.DateTimeField(
        auto_now=True,
    )
    last_updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pump_type_updated_user",
    )

    def __str__(self):
        return (
            "تیپ "
            + self.type_name
            + " از مدل "
            + self.main_model.model_name_fa
        )


class Product(models.Model):
    MOTOR_PHASE_CHOICES = [
        ("1 ph", "1 ph"),
        ("3 ph", "3 ph"),
    ]
    MOTOR_RPM_CHOICES = [
        ("1450 rpm", "1450 rpm"),
        ("2900 rpm", "2900 rpm"),
        ("2800 rpm", "2800 rpm"),
    ]
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    main_model = models.ForeignKey(
        MainModel,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="نام مدل اصلی پمپ",
    )
    usage = models.ManyToManyField(Usage)
    sub_usage = models.ManyToManyField(SubUsage)
    pump_type = models.ForeignKey(
        PumpType,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="تیپ پمپ",
    )
    pump_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name="نام محصول",
        unique=True,
    )
    pump_image = models.ImageField(
        upload_to=path_and_rename_image,
        help_text="تصویر الکتروپمپ",
        verbose_name="تصویر الکتروپمپ",
    )
    NPSH_diagram_image = models.ImageField(
        upload_to=path_and_rename_image,
        help_text="نمودار NPSH",
        verbose_name="نمودار NPSH",
    )
    power_diagram_image = models.ImageField(
        upload_to=path_and_rename_image,
        help_text="نمودار توان",
        verbose_name="نمودار توان",
    )
    max_head = models.FloatField()
    max_flow = models.FloatField()
    motor_ph = models.CharField(
        max_length=4,
        choices=MOTOR_PHASE_CHOICES,
        null=True,
        blank=True,
    )
    motor_rpm = models.CharField(
        max_length=8,
        choices=MOTOR_RPM_CHOICES,
        null=True,
        blank=True,
    )
    pump_technical_datasheet_fa = models.ImageField(
        upload_to=path_and_rename_image,
        help_text="کاتالوگ تگ برگ فارسی محصول",
        verbose_name="کاتالوگ تگ برگ فارسی محصول",
        null=True,
    )
    pump_technical_datasheet_en = models.ImageField(
        upload_to=path_and_rename_image,
        help_text="کاتالوگ تگ برگ انگلیسی محصول",
        verbose_name="کاتالوگ تگ برگ انگلیسی محصول",
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_created_user",
    )
    last_updated_at = models.DateTimeField(
        auto_now=True,
    )
    last_updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="product_updated_user",
    )

    def __str__(self):
        return self.pump_name


class HeadFlowDataset(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    head = models.FloatField()
    flow = models.FloatField()

    def __str__(self):
        return self.product.pump_name
