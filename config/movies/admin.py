from django.contrib import admin

from .models import *


class FilmsAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'rating']

class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating']
    prepopulated_fields = {'slug': ('title',)}

class CartoonsAdmin(admin.ModelAdmin):
    list_display = ['title', 'rating']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Films, FilmsAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Cartoons, CartoonsAdmin)
admin.site.register(Genre)
admin.site.register(Country)
admin.site.register(FilmsReview)
admin.site.register(SeriesReview)
admin.site.register(CartoonsReview)
