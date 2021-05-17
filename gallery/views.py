from django.shortcuts import render, redirect
from .models import Location, Category, Image
# Create your views here.

def home(request):
    location = request.GET.get('location')
    if location is None:
        gallery = Image.objects.all()
    else:
        gallery = Image.objects.filter(location__name=location)

    location = Location.objects.all()
    categories = Category.objects.all()

    return render(request, 'home.html', {"galleries": gallery, "locations": location, "categories": categories})

def viewPhoto(request, pk):
    photo =Image.objects.get(id=pk)
    return render(request, 'photo.html', {"photo": photo})
