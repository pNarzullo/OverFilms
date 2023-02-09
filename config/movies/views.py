from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import *
from django.views.generic.base import View

from .models import *


@login_required(login_url='/users/sign_in')
def base(request):
    search_query = request.GET.get('search','')

    if search_query:
        movies = Films.objects.filter(title__icontains=search_query)
        series = Series.objects.filter(title__icontains=search_query)
        cartoons = Cartoons.objects.filter(title__icontains=search_query)
    else:
        movies = Films.objects.all
        series = Series.objects.all
        cartoons = Cartoons.objects.all

    genres = Genre.objects.all

    return render(request, 'movies/movies.html', {'movies': movies, 'series': series, 'cartoons': cartoons, 'genres': genres})


def authors(request):
    return render(request, 'movies/authors.html')


def m_details(request, m_slug):
    movie = get_object_or_404(Films, slug=m_slug)
    return render(request, 'movies/m_details.html',  {'movie': movie})


def s_details(request, s_slug):
    series = get_object_or_404(Series, slug=s_slug)
    return render(request, 'movies/s_details.html',  {'series': series})
    

def c_details(request, c_slug):
    cartoon = get_object_or_404(Cartoons, slug=c_slug)
    return render(request, 'movies/c_details.html',  {'cartoon': cartoon})


    