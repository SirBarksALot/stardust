from django.urls import path
from .views import ChallengeView

urlpatterns = [
    # path('list', views.index, name='list'),
    path('create', ChallengeView.as_view(), name='create'),
]
