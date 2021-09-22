from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.forms import fields


class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email', 'password1' ,'password2']