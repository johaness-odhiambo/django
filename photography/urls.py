from django.urls import path
from . import views

app_name= 'photography'

urlpatterns = [
    path('home/', views.home_page, name="home" ),
    path('about/', views.about_page , name="about"),
    path('contact/', views.contact_page , name="contact"),
    path('services/', views.services_page, name="services"),
    path('starter/', views.starter_page , name="starter" ),
    path('gallery', views.gallery_page , name="gallery"),
    path('gallery-single/', views.gallery_single, name="gallery_single")
]