from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dogs/', views.dogs_index, name='dogs_index'),
  path('dogs/<int:dog_id>/', views.dogs_detail, name='dogs_detail'),
  path('dogs/create', views.DogCreate.as_view(), name='dogs_create'),
]