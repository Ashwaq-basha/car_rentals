from dataclasses import field
from importlib import import_module
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class regs(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']