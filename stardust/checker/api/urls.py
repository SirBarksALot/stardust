from django.urls import path
from .views import CheckView

urlpatterns = [
    path('ssl', CheckView.as_view(), name='check'),
]
