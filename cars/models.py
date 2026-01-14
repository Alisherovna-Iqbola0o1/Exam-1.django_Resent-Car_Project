from django.db import models

# Create your models here.

class CarCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('rented', 'Rented'),
    )

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    seats = models.PositiveIntegerField()
    max_rent_days = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    categories = models.ManyToManyField(CarCategory)

    def __str__(self):
        return f"{self.name} ({self.brand})"
