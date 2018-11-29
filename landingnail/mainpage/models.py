from django.db import models

class About (models.Model):
    name = models.CharField("название", max_length=50)
    privet = models.CharField("приветствие", max_length=30)
    description = models.TextField("описание")

    photo = models.ImageField("фотография", upload_to="mainpage/photos", default="", blank=True)

    class Meta:
        verbose_name = "главная"
        verbose_name_plural = "главная"


    def __str__(self):
            return self.name