from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def sign_up(request):
   if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user)
           return redirect('users:sign_in')
   form = UserCreationForm()
   return render(request, 'users/sign_up.html', {'form': form})


def sign_in(request):
   if request.method == 'POST':
       form = AuthenticationForm(data=request.POST)
       if form.is_valid():
           user = form.get_user()
           login(request, user)
           return redirect('movies:base')
   form = AuthenticationForm()
   return render(request, 'users/sign_in.html', {'form': form})


def sign_out(request):
   logout(request)
   return redirect('users:sign_in')