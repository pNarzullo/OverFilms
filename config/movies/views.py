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


class FilmsAddReview(View):
    def post(self, request, pk):
        form = FilmsReviewForm(request.POST)
        movie = Films.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()

        return redirect("movies:base")
    

class SeriesAddReview(View):
    def post(self, request, pk):
        form = SeriesReviewForm(request.POST)
        series = Series.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.series = series
            form.save()

        return redirect("movies:base")
    

class CartoonsAddReview(View):
    def post(self, request, pk):
        form = CartoonsReviewForm(request.POST)
        cartoon = Cartoons.objects.get(id=pk)

        if form.is_valid():
            form = form.save(commit=False)
            form.cartoon = cartoon
            form.save()

        return redirect("movies:base")
    

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

    return render(request, 'movies/all_films.html', {'films':films})


def all_series(request):
    series = Series.objects.all()

    return render(request, 'movies/all_series.html', {'series':series})


def all_cartoons(request):
    cartoons = Cartoons.objects.all()

    return render(request, 'movies/all_cartoons.html', {'cartoons':cartoons})