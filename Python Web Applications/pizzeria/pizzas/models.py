from django.db import models

class Pizza(models.Model):
	"""A type of pizza."""
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Topping(models.Model):
	"""A pizza topping."""
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	name = models.CharField(max_length=300)

	def __str__(self):
		return self.name
