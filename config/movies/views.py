from django.views.generic import ListView
from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db.models import Q
from .forms import *
from django.views.generic.base import View
from .models import *


def base(request):
    search_query = request.GET.get('search', '').strip()

    if search_query: 
        movies = Films.objects.filter(title__icontains=search_query)
        series = Series.objects.filter(title__icontains=search_query)
        cartoons = Cartoons.objects.filter(title__icontains=search_query)
    else:
        movies = Films.objects.all()
        series = Series.objects.all()
        cartoons = Cartoons.objects.all()
        
    genres = Genre.objects.all()
    
    return render(request, 'movies/movies.html', {'movies': movies, 'series': series, 'cartoons': cartoons, 'genres': genres})


def authors(request):
    return render(request, 'movies/authors.html')


def m_details(request, m_slug):
    movie = get_object_or_404(Films, slug=m_slug)

    movies = Films.objects.order_by('?')
    genres = Genre.objects.all()

    return render(request, 'movies/m_details.html',  {'movie': movie, 'movies': movies, 'genres':genres})


def s_details(request, s_slug):
    series = get_object_or_404(Series, slug=s_slug)

    series_ = Series.objects.order_by('?')
    genres = Genre.objects.all

    return render(request, 'movies/s_details.html',  {'series': series, 'series_': series_, 'genres':genres})
    

def c_details(request, c_slug):
    cartoon = get_object_or_404(Cartoons, slug=c_slug)

    cartoons = Cartoons.objects.order_by('?')
    genres = Genre.objects.all()

    return render(request, 'movies/c_details.html',  {'cartoon': cartoon, 'cartoons': cartoons, 'genres':genres})


class FilmsAddReview(View):
    def post(self, request, pk):
        form = FilmsReviewForm(request.POST)
        movie = get_object_or_404(Films, id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()

        return redirect("movies:m_details", movie.slug)
    

class SeriesAddReview(View):
    def post(self, request, pk):
        form = SeriesReviewForm(request.POST)
        series = get_object_or_404(Series, id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.series = series
            form.save()

        return redirect("movies:s_details", series.slug)
    

class CartoonsAddReview(View):
    def post(self, request, pk):
        form = CartoonsReviewForm(request.POST)
        cartoon = get_object_or_404(Cartoons, id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.cartoon = cartoon
            form.save()

        return redirect("movies:c_details", cartoon.slug)
    

def Filmslike(request, slug):
    movie = get_object_or_404(Films, slug=slug)

    if request.user not in movie.likes.all():
       movie.likes.add(request.user)
       movie.dislikes.remove(request.user)
    elif request.user in movie.likes.all():
       movie.likes.remove(request.user)
    return redirect('movies:m_details', m_slug=slug)


def Filmsdislike(request, slug):
    movie = get_object_or_404(Films, slug=slug)

    if request.user not in movie.dislikes.all():
       movie.dislikes.add(request.user)
       movie.likes.remove(request.user) 
    elif request.user in movie.dislikes.all():
       movie.dislikes.remove(request.user)
    return redirect('movies:m_details', m_slug=slug)


def Serieslike(request, slug):
    series = get_object_or_404(Series, slug=slug)

    if request.user not in series.likes.all():
       series.likes.add(request.user)
       series.dislikes.remove(request.user)
    elif request.user in series.likes.all():
       series.likes.remove(request.user)
    return redirect('movies:s_details', s_slug=slug)


def Seriesdislike(request, slug):
    series = get_object_or_404(Series, slug=slug)

    if request.user not in series.dislikes.all():
       series.dislikes.add(request.user)
       series.likes.remove(request.user) 
    elif request.user in series.dislikes.all():
       series.dislikes.remove(request.user)
    return redirect('movies:s_details', s_slug=slug)


def Cartoonslike(request, slug):
    cartoon = get_object_or_404(Cartoons, slug=slug)

    if request.user not in cartoon.likes.all():
       cartoon.likes.add(request.user)
       cartoon.dislikes.remove(request.user)
    elif request.user in cartoon.likes.all():
       cartoon.likes.remove(request.user)
    return redirect('movies:c_details', c_slug=slug)


def Cartoonsdislike(request, slug):
    cartoon = get_object_or_404(Cartoons, slug=slug)

    if request.user not in cartoon.dislikes.all():
       cartoon.dislikes.add(request.user)
       cartoon.likes.remove(request.user) 
    elif request.user in cartoon.dislikes.all():
       cartoon.dislikes.remove(request.user)
    return redirect('movies:c_details', c_slug=slug)



def all_films(request):
    films = Films.objects.all()
    genres = Genre.objects.all

    return render(request, 'movies/all_films.html', {'films':films, 'genres':genres})


def all_series(request):
    series = Series.objects.all()
    genres = Genre.objects.all

    return render(request, 'movies/all_series.html', {'series':series, 'genres':genres})


def all_cartoons(request):
    cartoons = Cartoons.objects.all()
    genres = Genre.objects.all()

    return render(request, 'movies/all_cartoons.html', {'cartoons':cartoons, 'genres':genres})


def m_genres(request, g_slug):
    genres = get_object_or_404(Genre, slug=g_slug)

    films = Films.objects.filter(genres=genres)


    return render(request, 'movies/m_genres.html', {'films': films, 'genres': genres})


def s_genres(request, g_slug):
    genres = get_object_or_404(Genre, slug=g_slug)

    series = Series.objects.filter(genres=genres)


    return render(request, 'movies/s_genres.html', {'series': series, 'genres': genres})


def c_genres(request, g_slug):
    genres = get_object_or_404(Genre, slug=g_slug)

    cartoons = Cartoons.objects.filter(genres=genres)


    return render(request, 'movies/c_genres.html', {'cartoons': cartoons, 'genres': genres})



# someCustomFunction
# some-custom-function
# Some_Custom_Function

# some_custom_function
# SomeCustomFunction
# SOME_CUSTOM_FUNCTION
