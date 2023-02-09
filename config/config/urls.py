from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('movies.urls', 'config'), namespace='movies')),
    path('users/', include(('users.urls', 'config'), namespace='users')),
]
