from django.shortcuts import render
from django.shortcuts import redirect

from .forms import PhotoForm
from .models import Photo
def upload_file(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = Photo.objects.all().last()
            return redirect(img.image.url)
    else:
        form = PhotoForm()
    return render(request, 'gallery/thumb_add.html', {'form': form})

def gallery(request):
    
    img = Photo.objects.all()
    return render(request, 'gallery/thumb.html', {'img': img})