from django.conf.urls import url
from gallery import  views

urlpatterns = [
   
   url(r'^add/$', views.upload_file, name='add'),
   url(r'^$', views.gallery, name='gallery'),
   
   ]