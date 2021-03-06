from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from account.models import NewUser


class CIModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        pass
