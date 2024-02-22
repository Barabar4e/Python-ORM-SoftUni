from django.core.exceptions import ValidationError


def name_validator(plant_name):
	for ch in plant_name:
		if not ch.isalpha():
			raise ValidationError("Plant name should contain only letters!")

