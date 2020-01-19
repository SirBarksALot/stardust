from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Graph-home'),
    path('about/', views.about, name='Graph-about'),
]