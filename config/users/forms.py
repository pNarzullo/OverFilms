from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from movies.bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Create username')
    email = forms.EmailField(label='Write email address')
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Create password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Write username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Write password')

    class Meta:
        model = User
        fields = ['username', 'password']
