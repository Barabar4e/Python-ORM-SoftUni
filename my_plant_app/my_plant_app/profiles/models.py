from django.core.validators import MinLengthValidator
from django.db import models
from my_plant_app.profiles.validators import name_validator


class Profile(models.Model):
	MIN_USERNAME_LENGTH = 2
	MAX_USERNAME_LENGTH = 10
	MAX_FIRST_NAME_LENGTH = 20
	MAX_LAST_NAME_LENGTH = 20

	username = models.CharField(
		max_length=MAX_USERNAME_LENGTH,
		null=False,
		blank=False,
		validators=(
			MinLengthValidator(MIN_USERNAME_LENGTH),
		),
		verbose_name="Username"
	)

	first_name = models.CharField(
		max_length=MAX_FIRST_NAME_LENGTH,
		validators=(
			# TODO check if validator is working
			name_validator,
		),
		null=False,
		blank=False,
		verbose_name="First Name"
	)

	last_name = models.CharField(
		max_length=MAX_LAST_NAME_LENGTH,
		validators=(
			# TODO check if validator is working
			name_validator,
		),
		null=False,
		blank=False,
		verbose_name="Last Name"
	)

	profile_picture = models.URLField(
		null=True,
		blank=True,
		verbose_name="Profile Picture"
	)
