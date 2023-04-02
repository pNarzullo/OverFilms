from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from movies.bulma_mixin import BulmaMixin


class SignUpForm(BulmaMixin, UserCreationForm):
    username = forms.CharField(label='Create username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Write email address', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Create password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Repeat password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        }


class SignInForm(BulmaMixin, AuthenticationForm):
    username = forms.CharField(label='Enter username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
