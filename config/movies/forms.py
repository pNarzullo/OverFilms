from django import forms

from .models import *


class FilmsReviewForm(forms.ModelForm):

    class Meta:
        model = FilmsReview
        fields = ('m_name', 'm_text')

class SeriesReviewForm(forms.ModelForm):

    class Meta:
        model = SeriesReview
        fields = ('s_name', 's_text')

class CartoonsReviewForm(forms.ModelForm):

    class Meta:
        model = CartoonsReview
        fields = ('c_name', 'c_text')


