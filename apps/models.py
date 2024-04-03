from django.db import models


# Create your models here.

class Sheep(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='ism')
    last_name = models.CharField(max_length=50, verbose_name='familya')
    address = models.CharField(max_length=50, verbose_name='joylashuv')
    photo = models.ImageField(verbose_name='rasim')
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=17)


