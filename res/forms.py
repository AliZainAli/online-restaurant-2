from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm




class SignUpForm(UserCreationForm):
    #password = forms.CharField(widget=forms.PasswordInput)
    mobile = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile', ]



