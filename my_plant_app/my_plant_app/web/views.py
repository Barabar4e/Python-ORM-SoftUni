from django.shortcuts import render

from my_plant_app.common.profile_helpers import get_profile


# def create_profile(request):
# 	pass


def index(request):
	profile = get_profile()

	context = {"profile": profile}

	if profile is None:
		return (request, "we")
	else:
		return render(request, "web/home-page.html")
