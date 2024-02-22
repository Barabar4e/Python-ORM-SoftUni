from django.core.validators import MinValueValidator
from django.db import models

from my_music.profiles.models import Profile


class Genre(models.TextChoices):
	Pop_Music = "GENRE_POP"
	Jazz_Music = "Jazz Music"
	R_N_B_Music = "R&B Music"
	Rock_Music = "Rock Music"
	Country_Music = "Country Music"
	Dance_Music = "Dance Music"
	Hip_Hop_Music = "Hip Hop Music"
	Other = "Other"


class Album(models.Model):
	MAX_NAME_LENGTH = 30
	MAX_ARTIST_NAME_LENGTH = 30
	MAX_GENDER_LENGTH = 30

	MIN_PRICE = 0.0

	name = models.CharField(
		max_length=MAX_NAME_LENGTH,
		unique=True,
		null=False,
		blank=False,
		verbose_name="Album name:",
	)

	artist_name = models.CharField(
		max_length=MAX_ARTIST_NAME_LENGTH,
		null=False,
		blank=False,
		verbose_name="Artist:",
	)

	genre = models.CharField(
		max_length=MAX_GENDER_LENGTH,
		null=False,
		blank=False,
		choices=Genre.choices,
		verbose_name="Genre:",
	)
	description = models.TextField(
		null=True,
		blank=True,
		verbose_name="Description:",
	)

	image_url = models.URLField(
		null=False,
		blank=False,
		verbose_name="Image URL:",
	)

	price = models.FloatField(
		null=False,
		blank=False,
		validators=(
			MinValueValidator(MIN_PRICE),
		),
		verbose_name="Price:",
	)

	owner = models.ForeignKey(
		Profile,
		on_delete=models.CASCADE,
	)
