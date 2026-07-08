from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path('dash/', views.dashboard, name='dash')
   
]