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

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "categories": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

