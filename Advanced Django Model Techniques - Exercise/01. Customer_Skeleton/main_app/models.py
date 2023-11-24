from decimal import Decimal

from django.contrib.postgres.search import SearchVectorField
from django.db import models

from main_app.mixins import RechargeEnergyMixin
from main_app.validators import name_validator, age_validator, phone_number_validator, author_length_validator, \
	isbn_length_validator, director_length_validator, artist_length_validator


class Customer(models.Model):
	name = models.CharField(
		max_length=100,
		validators=[
			name_validator,
		]
	)

	age = models.PositiveIntegerField(
		validators=[
			age_validator
		]
	)

	email = models.EmailField(
		error_messages={'invalid': 'Enter a valid email address'}
	)

	phone_number = models.CharField(
		max_length=13,
		validators=[
			phone_number_validator
		]
	)

	website_url = models.URLField(
		error_messages={'invalid': 'Enter a valid URL'}
	)


class BaseMedia(models.Model):

	class Meta:
		abstract = True
		ordering = ['-created_at', 'title']

	title = models.CharField(
		max_length=100,
	)

	description = models.TextField()

	genre = models.CharField(
		max_length=50,
	)

	created_at = models.DateTimeField(
		auto_now=True,
	)


class Book(BaseMedia):

	class Meta(BaseMedia.Meta):
		verbose_name = 'Model Book'
		verbose_name_plural = 'Models of type - Book'

	author = models.CharField(
		max_length=100,
		validators=[
			author_length_validator,
		]
	)

	isbn = models.CharField(
		max_length=20,
		unique=True,
		validators=[
			isbn_length_validator,
		]
	)


class Movie(BaseMedia):

	class Meta(BaseMedia.Meta):
		verbose_name = 'Model Movie'
		verbose_name_plural = 'Models of type - Movie'

	director = models.CharField(
		max_length=100,
		validators=[
			director_length_validator,
		]
	)


class Music(BaseMedia):

	class Meta(BaseMedia.Meta):
		verbose_name = 'Model Music'
		verbose_name_plural = 'Models of type - Music'

	artist = models.CharField(
		max_length=100,
		validators=[
			artist_length_validator,
		]
	)


class Product(models.Model):

	name = models.CharField(
		max_length=100,
	)

	price = models.DecimalField(
		max_digits=10,
		decimal_places=2,
	)

	def calculate_tax(self):
		tax = self.price * Decimal(0.08)

		return tax

	@staticmethod
	def calculate_shipping_cost(weight: Decimal):
		shipping_cost = weight * Decimal(2.00)

		return shipping_cost

	def format_product_name(self):
		return f"Product: {self.name}"


class DiscountedProduct(Product):

	class Meta:
		proxy = True

	def calculate_price_without_discount(self):
		return self.price * Decimal(1.20)

	def calculate_tax(self):
		return self.price * Decimal(0.05)

	@staticmethod
	def calculate_shipping_cost(weight: Decimal):
		return weight * Decimal(1.50)

	def format_product_name(self):
		return f"Discounted Product: {self.name}"


class Hero(models.Model, RechargeEnergyMixin):
	name = models.CharField(
		max_length=100,
	)

	hero_title = models.CharField(
		max_length=100,
	)

	energy = models.PositiveIntegerField()


class SpiderHero(Hero):

	class Meta:
		proxy = True

	def swing_from_buildings(self):
		self.energy -= 80

		if self.energy <= 0:
			return f"{self.name} as Spider Hero is out of web shooter fluid"

		self.save()
		return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):

	class Meta:
		proxy = True

	def run_at_super_speed(self):
		self.energy -= 65

		if self.energy <= 0:
			return f"{self.name} as Flash Hero needs to recharge the speed force"

		super().save()
		return f"{self.name} as Flash Hero runs at lightning speed, saving the day"


class Document(models.Model):
	title = models.CharField(
		max_length=200,
	)

	content = models.TextField()

	search_vector = SearchVectorField(
		null=True,
	)