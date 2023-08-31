from django.db import models
from django.db.models import Sum


# Create your models here.

class Products(models.Model):
    idnumber = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=7)
    manufacturedate = models.CharField(max_length=7)
    picture = models.ImageField(blank=True, upload_to='images/')
    price = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Mobiles(Products):
    cpu = models.CharField(max_length=7)
    gpu = models.CharField(max_length=7)
    monitor = models.CharField(max_length=7)
    monitorsize = models.IntegerField()


class Sabadekharid(Products):
    totalprice = models.IntegerField(default=0)

    def Aggregate(self):
        total = Sabadekharid.objects.aggregate(Sum('price'))
        return total