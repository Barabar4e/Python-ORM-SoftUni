import re

from django.core.exceptions import ValidationError


def name_validator(value):
	for ch in value:
		if not (ch.isalpha() or ch.isspace()):
			raise ValidationError("Name can only contain letters and spaces")


def age_validator(value):
	if value < 18:
		raise ValidationError("Age must be greater than 18")


def phone_number_validator(value):
	if not re.match(r'^\+359\d{9}$', value):
		raise ValidationError("Phone number must start with a '+359' followed by 9 digits")


def author_length_validator(value):
	if len(value) < 5:
		raise ValidationError("Author must be at least 5 characters long")


def isbn_length_validator(value):
	if len(value) < 6:
		raise ValidationError("ISBN must be at least 6 characters long")


def director_length_validator(value):
	if len(value) < 8:
		raise ValidationError("Director must be at least 8 characters long")


def artist_length_validator(value):
	if len(value) < 9:
		raise ValidationError("Artist must be at least 9 characters long")

