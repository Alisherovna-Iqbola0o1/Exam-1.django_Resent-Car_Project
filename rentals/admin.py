from django.contrib import admin
from .models import Rental, RentalItem

# Register your models here.

admin.site.register(Rental)
admin.site.register(RentalItem)
