from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('city/<slug:slug>/', views.city_detail, name='city_detail'),
    path('place/<slug:slug>/', views.place_detail, name='place_detail'),
    path('random/', views.random_destination, name='random_destination'),
]