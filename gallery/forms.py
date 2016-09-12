from django import forms
from .models import Photo

class PhotoForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Photo
        fields = ['image', 'comment']
        