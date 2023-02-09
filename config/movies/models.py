from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    country = models.CharField('Страна', max_length=30)

    def __str__(self):
        return self.country

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class Genre(models.Model):
    genre = models.CharField('Название жанра', max_length=20)

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Films(models.Model):
    title = models.CharField('Название', max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField('Постер', upload_to='static/app/img')
    desc = models.TextField('Описание')
    video = models.FileField('Видео', upload_to='static/app/video')
    wiki = models.TextField('Подробнее о фильме')
    poster = models.ImageField('Превью', upload_to='static/app/img')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year_n_duration = models.CharField('Год и продолжительность', max_length=255)
    rating = models.CharField('Рейтинг (IMDb)', max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'


class Series(models.Model):
    title = models.CharField('Название', max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField('Постер', upload_to='static/app/img')
    desc = models.TextField('Описание')
    video = models.FileField('Видео', upload_to='static/app/video')
    wiki = models.TextField('Подробнее о фильме')
    poster = models.ImageField('Превью', upload_to='static/app/img')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year_n_duration = models.CharField('Год и продолжительность', max_length=255)
    rating = models.CharField('Рейтинг (IMDb)', max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'


class Cartoons(models.Model):
    title = models.CharField('Название', max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField('Постер', upload_to='static/app/img')
    desc = models.TextField('Описание')
    video = models.FileField('Видео', upload_to='static/app/video')
    wiki = models.TextField('Подробнее о фильме')
    poster = models.ImageField('Превью', upload_to='static/app/img')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year_n_duration = models.CharField('Год и продолжительность', max_length=255)
    rating = models.CharField('Рейтинг (IMDb)', max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cartoon'
        verbose_name_plural = 'Cartoons'











# python manage.py migrate --run-syncdb