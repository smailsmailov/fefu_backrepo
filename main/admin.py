from django.contrib import admin
from .models import Person , Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name","date")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    exclude = ("password",)
    search_fields = ("name","company__date",)
    list_display = ("id","name","company__date","cat_name",)