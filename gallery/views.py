from django.shortcuts import render
from .models import Location, Category, Image
# Create your views here.

def home(request):
    gallery = Image.objects.all()
    location = Location.objects.all()
    category = Category.objects.all()
    return render(request, 'home.html', {"galleries": gallery, "location": location, "category": category})
