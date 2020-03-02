from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),
    # The index page
    path('', views.index, name='index'),
]
