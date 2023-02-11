from django.urls import path

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('m_details/<slug:m_slug>/', views.m_details, name='m_details'),
    path('s_details/<slug:s_slug>/', views.s_details, name='s_details'),
    path('c_details/<slug:c_slug>/', views.c_details, name='c_details'),
    path('authors', views.authors, name='authors'),
    path('m_details/review/<int:pk>/', views.FilmsAddReview.as_view(), name='m_add_review'),
    path('s_details/review/<int:pk>/', views.SeriesAddReview.as_view(), name='s_add_review'),
    path('c_details/review/<int:pk>/', views.CartoonsAddReview.as_view(), name='c_add_review'),
    path('<slug:slug>/m_like', views.Filmslike, name='m_like'),
    path('<slug:slug>/m_dislike', views.Filmsdislike, name='m_dislike'),
    path('<slug:slug>/s_like', views.Serieslike, name='s_like'),
    path('<slug:slug>/s_dislike', views.Seriesdislike, name='s_dislike'),
    path('<slug:slug>/c_like', views.Cartoonslike, name='c_like'),
    path('<slug:slug>/c_dislike', views.Cartoonsdislike, name='c_dislike'),
    path('all_films/', views.all_films, name="all_films"),
    path('all_series/', views.all_series, name="all_series"),
    path('all_cartoons/', views.all_cartoons, name="all_cartoons"),
]