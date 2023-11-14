import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom


def create_pet(name: str, species: str):
	Pet.objects.create(
		name=name,
		species=species
	)

	return f"{name} is a very cute {species}!"


def create_artifact(
		name: str,
		origin: str,
		age: int,
		description: str,
		is_magical: bool
):
	Artifact.objects.create(
		name=name,
		origin=origin,
		age=age,
		description=description,
		is_magical=is_magical
	)

	return f"The artifact {name} is {age} years old!"


def delete_all_artifacts():
	Artifact.objects.all().delete()


def show_all_locations():
	locations = Location.objects.all().order_by('-id')

	return '\n'.join(str(x)for x in locations)


def new_capital():
	Location.objects.all().filter(pk=1).update(is_capital=True)


def get_capitals():
	return Location.objects.filter(is_capital=True).values("name")


def delete_first_location():
	Location.objects.first().delete()


def apply_discount():
	cars = Car.objects.all()

	for car in cars:
		car_percentage_off = sum(int(x) for x in str(car.year)) / 100
		discount = float(car.price) * car_percentage_off
		car.price_with_discount = float(car.price) - discount
		car.save()


def get_recent_cars():
	return Car.objects.filter(year__gte=2020).values('model', 'price_with_discount')


def delete_last_car():
	Car.objects.last().delete()


def show_unfinished_tasks():
	unfinished_tasks = Task.objects.filter(is_finished=False)

	return '\n'.join(str(task)for task in unfinished_tasks)


def complete_odd_tasks():
	tasks = Task.objects.all()

	for task in tasks:
		if task.id % 2 != 0:
			task.is_finished = True
			task.save()


def encode_and_replace(text: str, task_title: str):
	tasks_with_tittle = Task.objects.filter(title=task_title)
	decoded_task = ''.join(chr(ord(ch) - 3) for ch in text)

	for task in tasks_with_tittle:
		task.description = decoded_task
		task.save()


encode_and_replace("Zdvk#wkh#glvkhv$", "Simple Task")


def get_deluxe_rooms():
	deluxe_rooms = HotelRoom.objects.filter(room_type='Deluxe')
	even_id_deluxe_rooms = []
	for room in deluxe_rooms:
		if room.id % 2 == 0:
			even_id_deluxe_rooms.append(str(room))

	return '\n'.join(even_id_deluxe_rooms)


def increase_room_capacity():
	rooms = HotelRoom.objects.all().order_by("id")

	previous_room_capacity = None

	for room in rooms:
		if not room.is_reserved:
			continue

		if previous_room_capacity:
			room.capacity += previous_room_capacity
		else:
			room.capacity += room.id

		previous_room_capacity = room.capacity

		room.save()


def reserve_first_room():
	first_room = HotelRoom.objects.first()
	first_room.is_reserved = True
	first_room.save()


def delete_last_room():
	last_room = HotelRoom.objects.last()

	if last_room.is_reserved:
		last_room.delete()