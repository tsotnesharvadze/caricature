from django.db import models


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images', null=False, blank=False)
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "no name"
