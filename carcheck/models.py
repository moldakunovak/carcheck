from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CarOwner(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

class Car(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, related_name='cars', blank=True, null=True, default='')
    name = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    image = models.ImageField(upload_to='cars', default='cars/cefzim_l6hc-o2.jpg')
    year = models.DateField()
    engine = models.FloatField()
    color = models.CharField(max_length=150)
    number = models.CharField(max_length=10, unique=True, null=True)


class CarImage(models.Model):
    image = models.ImageField(upload_to="cars")
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_images')


