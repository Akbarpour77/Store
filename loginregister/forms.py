from .models import Userprofile
from django import forms
from django.contrib.auth.models import User


class User_profile_info(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = '__all__'


class User_profile(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': "username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': "password"}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
