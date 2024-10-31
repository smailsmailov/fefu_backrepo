from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path("test/", views.test),
    path("test1/", views.test),
    path("test2/", views.test),
    path("test3/", views.test),
]
# python manage.py runserver