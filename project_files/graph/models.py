from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Item(models.Model):
    name = models.CharField(max_length=100)
    unique_name = models.CharField(max_length=100)
    description = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
