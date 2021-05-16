from django.contrib import admin
from .models import Location, Category, Image

# Register your models here.

class DisplayAdmin(admin.ModelAdmin):
    filter_horizontal =('category',)

admin.site.register(Location)
admin.site.register(Image, DisplayAdmin)
admin.site.register(Category)