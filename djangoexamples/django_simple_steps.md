 django-admin startproject project

# python manage.py migrate

# python manage.py runserver

# python manage.py creatsuperuser


# python manage.py startapp webapp

# settings.py

INSTALLED_APPS = [
    'webapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

project/webapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
 
def index(request):
    return  HttpResponse("<H2>HEY! Welcome to Django! </H2>")


project1/webapp/urls.py
from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
]


project1/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('blog_posts.urls','blog_posts'),namespace='blog_posts'))
]


# start the server

# cd top_level_project_directory
python manage.py runserver

# access the application from browser
http://localhost:8000

project1/webapp/models.py

from django.db import models

# Create your models here.
class blog_posts(models.Model):
    title = models.CharField(max_length=200)
    tag = models.CharField(max_length=50)
    author = models.CharField(max_length=120)
    class Meta:
        db_table="blog_posts"


