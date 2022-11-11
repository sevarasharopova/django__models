from django.db import models

class Animal(models.Model):
   turi = models.CharField(max_length=20)
   laqabi = models.CharField(max_length=10)
   yoshi = models.IntegerField(default=15)

def __str__(self):
    return f"{self.turi} {self.laqabi} {self.yoshi}"

class Institut(models.Model):
    shahar = models.CharField(max_length=10)
    yonalish = models.CharField(max_length=20)
    kurs = models.IntegerField(default=4)

def __str__(self):
    return f"{self.shahar} {self.yonalish} {self.kurs}"

class Flower(models.Model):
    nomi = models.CharField(max_length=10)
    rangi = models.CharField(max_length=10)
    hidi = models.CharField(max_length=10)


def __str__(self):
    return f"{self.nomi} {self.rangi} {self.hidi}"

