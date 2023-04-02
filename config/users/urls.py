from django.urls import path

from . import views

urlpatterns = [
    path('sign_up/', views.sign_up.as_view(), name='sign_up'),
    path('sign_in/', views.sign_in.as_view(), name='sign_in'),
path('sign_out/', views.sign_out, name='sign_out'),]