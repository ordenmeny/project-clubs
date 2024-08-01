from django.contrib.auth.forms import UserCreationForm

from .models import UserModel
from django import forms


class UserModelForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'age', 'city', 'skills']
