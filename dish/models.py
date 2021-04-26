from django.db import models

class Dish(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()

	class Meta:
		verbose_name= 'блюдо'
		verbose_name_plural = 'Блюда'

	def __str__(self):
		return self.name