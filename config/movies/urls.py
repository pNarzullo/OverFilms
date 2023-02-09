from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('m_details/<slug:m_slug>/', views.m_details, name='m_details'),
    path('s_details/<slug:s_slug>/', views.s_details, name='s_details'),
    path('c_details/<slug:c_slug>/', views.c_details, name='c_details'),
    path('authors', views.authors, name='authors'),
]