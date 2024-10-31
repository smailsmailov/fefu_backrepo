from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30 , default = "")
    id = models.AutoField(primary_key=True)
    password = models.TextField(max_length=250, default = "")
    cat_name = models.TextField(max_length=50 , default = "BARSIK")