from gallery.items.fields import ThumbnailImageField
from django.db import models


class Photo(models.Model):
    image = ThumbnailImageField(upload_to='photo')
    comment = models.CharField(max_length=250)
    
    def __str__(self):
        return self.image.name