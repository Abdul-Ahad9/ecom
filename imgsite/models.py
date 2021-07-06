from django.db import models


class Images(models.Model):
    image_id = models.AutoField
    title = models.CharField(max_length=20, default="")
    small_description = models.CharField(max_length=35, default="")
    image = models.ImageField(upload_to="imgsite/images", default="")
    category = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.title
