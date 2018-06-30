from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images', null=False, blank=False)
    name = models.CharField(max_length=255, default="", blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "no name"

    def get_image(self):
        return self.image.url
