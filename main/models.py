from django.db import models
import datetime

class Company(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField(default = datetime.date.today)

    class Meta:
        verbose_name = "Компании"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f"{self.name}"

class Person(models.Model):
    name = models.CharField(max_length=30 , default = "")
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Company ,default = "" ,  on_delete = models.CASCADE)
    password = models.TextField(max_length=250, default = "")
    cat_name = models.TextField(max_length=50 , default = "BARSIK")

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Человек"

    def __str__(self):
        return self.name