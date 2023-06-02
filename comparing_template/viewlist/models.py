from django.db import models

from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.CharField(max_length=250)
    store_link = models.URLField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.price} Created at: {self.created_at} Updated at: {self.updated_at}'
