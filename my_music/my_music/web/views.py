from django.shortcuts import render, redirect

from my_music.albums.models import Album
from my_music.common.profile_helpers import get_profile
from my_music.web.forms import CreateProfileForm


def create_profile(request):
	form = CreateProfileForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect("index")

	context = {
		"form": form,
		"no_nav": True,

	}
	return render(request, "web/home-no-profile.html", context)


def index(request):
	profile = get_profile()

	if profile is None:
		return create_profile(request)

	contex = {
		"albums": Album.objects.all(),
	}

	return render(request, "web/home-with-profile.html", contex)
