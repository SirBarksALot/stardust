from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Challenger-home'),
    path('about/', views.about, name='Challenger-about'),
]