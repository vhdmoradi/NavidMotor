from django.db import models


class Cities(models.Model):
    province = models.ForeignKey("Provinces", models.DO_NOTHING)
    name = models.CharField(max_length=255, db_collation="utf8mb3_unicode_ci")

    class Meta:
        db_table = "cities"
