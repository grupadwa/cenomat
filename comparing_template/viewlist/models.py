from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.CharField(max_length=250)
    store_link = models.URLField()

    def __str__(self):
        return f'{ self.name } { self.price }'