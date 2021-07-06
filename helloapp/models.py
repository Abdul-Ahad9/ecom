from django.db import models


class Data(models.Model):
    name = models.CharField(max_length=15, default="")
    body = models.CharField(max_length=15, default="")
    subtitle = models.CharField(max_length=35, default="")
    about_des = models.CharField(max_length=240, default="")
    about_ful_des = models.CharField(max_length=1200, default="")
    image1 = models.ImageField(upload_to="helloapp/images",default="")
    image_title1 = models.CharField(max_length=15, default="")
    image2 = models.ImageField(upload_to="helloapp/images",default="")
    image_title2 = models.CharField(max_length=15, default="")
    image3 = models.ImageField(upload_to="helloapp/images",default="")
    image_title3 = models.CharField(max_length=15, default="")




    def __str__(self):
        return self.name
