from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class AccountManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        # these 3 are validated in serializer, leaving it just in case
        if not username:
            raise ValueError('You must provide username.')
        if not email:
            raise ValueError('You must provide email.')
        if not username.isalnum():
            raise ValueError('Only alphanumeric character allowed in username.')

        user = self.model(
            username=username,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save()

        return user


class Account(AbstractBaseUser):
    class Meta:
        app_label = 'account'

    username = models.TextField(verbose_name='username', max_length=30, unique=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
