from django.core.validators import MinLengthValidator
from django.db import models


class PlantTypeChoices(models.TextChoices):
	Outdoor_Plants = "Outdoor Plants"
	Indoor_Plants = "Indoor Plants"


class PlantModel(models.Model):
	MAX_PLANT_TYPE_LENGTH = 14
	MIN_PLANT_NAME_LENGTH = 2
	MAX_PLANT_NAME_LENGTH = 20

	plant_type = models.CharField(
		max_length=MAX_PLANT_TYPE_LENGTH,
		null=False,
		blank=False,
		choices=PlantTypeChoices.choices,
		verbose_name="Plant Type",
	)

	plant_name = models.CharField(
		max_length=MAX_PLANT_NAME_LENGTH,
		null=False,
		blank=False,
		validators=(
			MinLengthValidator(MIN_PLANT_NAME_LENGTH),
		),
		verbose_name="Name"
	)

	image_url = models.URLField(
		null=False,
		blank=False,
		verbose_name="Image URL",
	)

	description = models.TextField(
		null=False,
		blank=False,
		verbose_name="Description",
	)

	price = models.FloatField(
		null=False,
		blank=False,
		verbose_name="Price",
	)
