from django.db import models
from django.core.validators import MaxValueValidator


class Dish(models.Model):
	name = models.CharField(max_length=255)
	price = models.IntegerField()
	is_vaialable = models.BooleanField(default=True)
	calories = models.IntegerField(blank=True, null=True, default=0, validators=[MaxValueValidator(10000)])
	class Meta:
		verbose_name= 'блюдо'
		verbose_name_plural = 'Блюда'

	def __str__(self):
		return self.name

