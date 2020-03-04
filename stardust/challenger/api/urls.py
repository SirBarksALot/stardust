from django.urls import path
from rest_framework.authtoken import views
from .views import IndexView


app_name = 'account'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
