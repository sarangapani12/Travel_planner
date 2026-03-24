from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import City, Place, Category, Country
import random

BUDGET_DATA = {
    'budget': {
        'food_min': 200, 'food_max': 500,
        'transport_min': 100, 'transport_max': 300,
        'entry_min': 50, 'entry_max': 200,
        'hotel_budget': '₹500 – ₹1,200',
        'hotel_mid': '₹1,200 – ₹3,000',
        'hotel_luxury': '₹3,000 – ₹8,000',
    },
    'medium': {
        'food_min': 500, 'food_max': 1500,
        'transport_min': 300, 'transport_max': 800,
        'entry_min': 100, 'entry_max': 500,
        'hotel_budget': '₹1,200 – ₹2,500',
        'hotel_mid': '₹2,500 – ₹6,000',
        'hotel_luxury': '₹6,000 – ₹20,000',
    },
    'luxury': {
        'food_min': 1500, 'food_max': 5000,
        'transport_min': 800, 'transport_max': 3000,
        'entry_min': 200, 'entry_max': 1000,
        'hotel_budget': '₹2,500 – ₹5,000',
        'hotel_mid': '₹5,000 – ₹15,000',
        'hotel_luxury': '₹15,000 – ₹50,000',
    },
}

def home(request):
    query = request.GET.get('q', '').strip()
    country_filter = request.GET.get('country', '')
    cities = City.objects.select_related('country').all()
    if query:
        cities = cities.filter(name__icontains=query)
    if country_filter:
        cities = cities.filter(country__id=country_filter)
    countries = Country.objects.all()
    return render(request, 'myapp/home.html', {
        'cities': cities,
        'countries': countries,
        'query': query,
        'selected_country': country_filter,
    })

def city_detail(request, slug):
    city = get_object_or_404(City, slug=slug)
    category_filter = request.GET.get('category', '')
    places = city.places.select_related('category').all()
    if category_filter:
        places = places.filter(category__id=category_filter)
    categories = Category.objects.all()
    budget = BUDGET_DATA.get(city.budget_level, BUDGET_DATA['medium'])
    total_min = budget['food_min'] + budget['transport_min'] + budget['entry_min']
    total_max = budget['food_max'] + budget['transport_max'] + budget['entry_max']
    return render(request, 'myapp/city_detail.html', {
        'city': city,
        'places': places,
        'categories': categories,
        'selected_category': category_filter,
        'budget': budget,
        'total_min': total_min,
        'total_max': total_max,
    })

def place_detail(request, slug):
    place = get_object_or_404(Place, slug=slug)
    images = place.images.all()
    related = Place.objects.filter(city=place.city).exclude(id=place.id)[:3]
    return render(request, 'myapp/place_detail.html', {
        'place': place,
        'images': images,
        'related': related,
    })

def random_destination(request):
    cities = list(City.objects.all())
    if cities:
        city = random.choice(cities)
        return redirect('city_detail', slug=city.slug)
    return redirect('home')