from django.db import models


class Challenge(models.Model):
    class Meta:
        app_label = 'challenger'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
