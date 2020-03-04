from django.contrib.auth.backends import ModelBackend


class EmailOrUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(request)
        print(kwargs)
        return None
