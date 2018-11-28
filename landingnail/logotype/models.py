from django.db import models

class Logo(models.Model):
    logoimg = models.ImageField("логотип", upload_to="logotype/photos", default="", blank=True)

    class Meta:
        verbose_name = "логотип"
        verbose_name_plural = "лого"
