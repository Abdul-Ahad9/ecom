from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=35, default="")
    video = models.FileField(upload_to="media/videosite", default="")

    def __str__(self):
        return self.title
