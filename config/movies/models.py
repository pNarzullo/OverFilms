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
    title = models.CharField('Название жанра', max_length=20)
    slug = models.SlugField(max_length=160, unique=True)
    desc = models.TextField('Описание')
    after_text = models.TextField('Подробнее о жанре')
    after_header = models.CharField('Заголовок', max_length=50)
    after_header_text = models.TextField('Про жанр на этом сайте')

    def __str__(self):
        return self.title

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
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year_n_duration = models.CharField('Год и продолжительность', max_length=255)
    rating = models.CharField('Рейтинг (IMDb)', max_length=10)
    likes = models.ManyToManyField(User, related_name='m_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='m_dislikes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Films'

    def total_dislikes(self):
        return self.dislikes.count()

    def total_likes(self):
        return self.likes.count()


class Series(models.Model):
    title = models.CharField('Название', max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField('Постер', upload_to='static/app/img')
    desc = models.TextField('Описание')
    video = models.FileField('Видео', upload_to='static/app/video')
    wiki = models.TextField('Подробнее о фильме')
    poster = models.ImageField('Превью', upload_to='static/app/img')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year_n_duration = models.CharField('Год и продолжительность', max_length=255)
    rating = models.CharField('Рейтинг (IMDb)', max_length=10)
    likes = models.ManyToManyField(User, related_name='s_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='s_dislikes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    def total_dislikes(self):
        return self.dislikes.count()

    def total_likes(self):
        return self.likes.count()


class Cartoons(models.Model):
    title = models.CharField('Название', max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    image = models.ImageField('Постер', upload_to='static/app/img')
    desc = models.TextField('Описание')
    video = models.FileField('Видео', upload_to='static/app/video')
    wiki = models.TextField('Подробнее о фильме')
    poster = models.ImageField('Превью', upload_to='static/app/img')
    genres = models.ManyToManyField(Genre, verbose_name='Genres')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year_n_duration = models.CharField('Год и продолжительность', max_length=255)
    rating = models.CharField('Рейтинг (IMDb)', max_length=10)
    likes = models.ManyToManyField(User, related_name='c_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='c_dislikes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cartoon'
        verbose_name_plural = 'Cartoons'

    def total_dislikes(self):
        return self.dislikes.count()

    def total_likes(self):
        return self.likes.count()


class FilmsReview(models.Model):
    m_name = models.CharField('Имя', max_length=100)
    m_email = models.EmailField('Электронная почта', null=True, blank=True)
    m_text = models.TextField('Ваш отзыв')
    movie = models.ForeignKey(Films, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.m_name} - {self.movie} - {self.m_text[:20]}..."

    class Meta:
        verbose_name = "Films Review"
        verbose_name_plural = "Films Reviews"


class SeriesReview(models.Model):
    s_name = models.CharField('Имя', max_length=100)
    s_email = models.EmailField('Электронная почта', null=True, blank=True)
    s_text = models.TextField('Ваш отзыв')
    series = models.ForeignKey(Series, verbose_name='Сериал', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.s_name} - {self.series} - {self.s_text[:20]}..."

    class Meta:
        verbose_name = "Series Review"
        verbose_name_plural = "Series Reviews"


class CartoonsReview(models.Model):
    c_name = models.CharField('Имя', max_length=100)
    c_email = models.EmailField('Электронная почта', null=True, blank=True)
    c_text = models.TextField('Ваш отзыв')
    cartoon = models.ForeignKey(Cartoons, verbose_name='Мультфильм', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.c_name} - {self.cartoon} - {self.c_text[:20]}..."

    class Meta:
        verbose_name = "Cartoons Review"
        verbose_name_plural = "Cartoons Reviews"

# python manage.py migrate --run-syncdb
