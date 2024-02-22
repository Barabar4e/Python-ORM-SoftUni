from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include('my_music.web.urls')),
    path("album/", include('my_music.albums.urls')),
    path("profiles/", include('my_music.profiles.urls')),
]
