from django.contrib import admin
from carcheck.models import Car, CarImage, CarOwner

admin.site.register(Car)
admin.site.register(CarImage)
admin.site.register(CarOwner)