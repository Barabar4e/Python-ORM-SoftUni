from my_music.profiles.models import Profile


def get_profile():
	return Profile.objects.first()