from django.db import models
from django.conf import settings
from cars.models import Car

# Create your models here.

User = settings.AUTH_USER_MODEL

class Rental(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('returned', 'Returned'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    rent_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.user} - {self.car}"


class RentalItem(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='items')
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    days = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
