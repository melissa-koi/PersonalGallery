from django.contrib import admin
from .models import Location, Category, Image

# Register your models here.

class DisplayAdmin(admin.ModelAdmin):
    admin.site.register(Location)
    admin.site.register(Category)
    admin.site.register(Image)