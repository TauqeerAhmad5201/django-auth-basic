from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('firstname', 'email',)  #option to show which field you want from CustomUser Model at Signup.

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('firstname', 'email',)