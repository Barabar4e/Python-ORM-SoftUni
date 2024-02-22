from django.core.exceptions import ValidationError


def name_validator(value):
	is_valid = value[0].isupper()

	if not is_valid:
		raise ValidationError("Your name must start with a capital letter!")
