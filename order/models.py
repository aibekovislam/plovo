from django.db import models
from django.contrib.auth.models import User
from dish.models import Dish

class Order(models.Model):
    user = models.ForeignKey(
        to = User,
        on_delete = models.SET_NULL,
        null=True, blank=True
    )
    dish = models.ForeignKey(
        to=Dish,
        on_delete=models.CASCADE
    )
    adress = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    discount = models.BooleanField(default=False)
    discount_sum = models.IntegerField()
    status = models.IntegerField(default=0, choices=(
        (0, 'Accepted'),
        (1, 'Done'),
        (2, 'Canceled'),
    ))


    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'



