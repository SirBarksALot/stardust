from django.urls import path
from rest_framework.authtoken import views
from .views import RegistrationView

app_name = 'account'

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', views.obtain_auth_token, name='login')
]
