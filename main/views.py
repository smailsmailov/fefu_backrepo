from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from django.utils.http import re 
from .models import Person , Company
from django.contrib.auth.models import User
from django.core import serializers

def test(request):

    

    data = serializers.serialize("json", Person.objects.all().fields())
    return JsonResponse(data , safe = False)