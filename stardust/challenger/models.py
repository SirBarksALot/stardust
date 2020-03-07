from django.db import models


class Challenge(models.Model):
    class Meta:
        app_label = 'challenger'

    name = models.TextField(default='', max_length=30)
    owner = models.TextField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
