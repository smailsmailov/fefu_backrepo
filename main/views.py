from django.shortcuts import render
from django.utils.http import re
from .models import Person
from django.contrib.auth.models import User


def test(request):
    if request.method == "GET":

        all_persons = User.objects.all()

        test = User.objects.filter(username = "admin")

        admin = test[0]

        admin.username = "DANIL"
        
        admin.save()

        print(admin.username)

        data = {
            "persons" : all_persons[0].username,
            "title": request.method ,
        }
        return render(request , "main.html" , data)
    if request.method == "POST":
        data = {
            "title": request ,
        }
        return render(request , "main.html" , data)
    