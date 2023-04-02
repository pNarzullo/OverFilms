from django import template

from ..models import Genre

register = template.Library()


@register.inclusion_tag('genres.html')
def genres():
    genres_list = Genre.objects.all()
    return {'genres': genres_list}
