from django.urls import path

from my_music.web.views import index, create_profile

urlpatterns = (
	path("", index, name="index"),
	path("create-profiles/", create_profile, name="create_profile"),
)
