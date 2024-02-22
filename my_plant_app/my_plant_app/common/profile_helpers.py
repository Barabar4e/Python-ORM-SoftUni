from my_plant_app.profiles.models import Profile


def get_profile():
	return Profile.objects.first()
