from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os

def _add_mini(s):
    parts = s.split('.')
    parts.insert(-1, 'mini')
    if parts[-1].lower() not in ['jpeg', 'jpg']:
        parts[-1] = 'jpeg'
    return '.'.join(parts)

class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_mini_path(self):
        return _add_mini(self.path)
    mini_path = property(_get_mini_path)
    
    def _get_mini_url(self):
        return _add_mini(self.url)
    mini_url = property(_get_mini_url)
    
    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)
        img.thumbnail(
            (self.field.mini_width, self.field.mini_height),
            Image.ANTIALIAS
        )
        img.save(self.mini_path, 'JPEG')
        
class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile
    def __init__(self, mini_width=250, mini_height=250, *args, **kwargs):
        self.mini_height = mini_height
        self.mini_width = mini_width
        super(ThumbnailImageField,self).__init__(*args, **kwargs)

 