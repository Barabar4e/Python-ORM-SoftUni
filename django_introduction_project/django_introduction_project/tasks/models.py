from django.db import models


class Task(models.Model):
	title = models.CharField(
		max_length=120
	)

	description = models.TextField()

	done = models.BooleanField(
		default=False,
	)

	def custom_method(self):
		return self.title + self.description
