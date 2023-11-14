import os
from datetime import date, timedelta

import django
from django.db.models import Sum, Count

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Song, Artist, Product, Review, DrivingLicense, Driver, Registration, Owner, \
	Car


def show_all_authors_with_their_books():
	authors_with_books = []

	authors = Author.objects.all().order_by('id')

	for author in authors:
		books = Book.objects.filter(author=author)

		if not books:
			continue

		titles = ', '.join(book.title for book in books)

		authors_with_books.append(f"{author.name} has written - {titles}!")

	return '\n'.join(authors_with_books)


def delete_all_authors_without_books():
	Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
	artist = Artist.objects.get(name=artist_name)
	song = Song.objects.get(title=song_title)

	artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
	artist = Artist.objects.get(name=artist_name)
	return artist.songs.all().order_by('id')


def remove_song_from_artist(artist_name: str, song_title: str):
	artist = Artist.objects.get(name=artist_name)
	song = Song.objects.get(title=song_title)

	artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
	product = Product.objects.get(name=product_name)
	all_reviews = product.reviews.all()

	ratings = sum(r.rating for r in all_reviews)
	average_rating = ratings / len(all_reviews)

	return average_rating


# product = Product.objects.annotate(
# 	ratings=Sum('review__rating'),
# 	num_reviews=Count('review')
# ).get(name=product_name)
#
# average_rating = product.ratings / product.num_reviews
#
# return average_rating


def get_reviews_with_high_ratings(threshold: int):
	return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
	return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
	Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
	licenses = DrivingLicense.objects.all().order_by('-license_number')

	return '\n'.join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date):
	end_date = due_date - timedelta(days=365)

	driver_with_expired_licenses = Driver.objects.filter(drivinglicense__issue_date__gt=end_date)

	return driver_with_expired_licenses


def register_car_by_owner(owner: Owner):
	registration_without_car = Registration.objects.filter(car__isnull=True).first()
	car_without_registration = Car.objects.filter(registration__isnull=True).first()

	car_without_registration.owner = owner
	car_without_registration.registration = registration_without_car

	car_without_registration.save()

	registration_without_car.registration_date = date.today()
	registration_without_car.car_without_registration = car_without_registration

	registration_without_car.save()

	return f"Successfully registered {car_without_registration.model} to {owner.name} with registration number {registration_without_car.registration_number}."


# Create instances of the Owner model
owner1 = Owner.objects.create(name='Ivelin Milchev')
owner2 = Owner.objects.create(name='Alice Smith')

# Create instances of the Car model and associate them with owners
car1 = Car.objects.create(model='Citroen C5', year=2004)
car2 = Car.objects.create(model='Honda Civic', year=2021)

# Create instances of the Registration model for the cars
registration1 = Registration.objects.create(registration_number='TX0044XA')
registration2 = Registration.objects.create(registration_number='XYZ789')

print(register_car_by_owner(owner1))
