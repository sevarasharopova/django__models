from django.db import models

class Kompyuter(models.Model):
    nomi = models.CharField(max_length=20)
    versiyasi = models.IntegerField(default=10)
    narxi = models.IntegerField(default=10)

def __str__(self):
    return f"{self.nomi} {self.versiyasi} {self.narxi}"


class Avtomobil(models.Model):
    turi = models.CharField(max_length=20)
    narxi = models.IntegerField(default=10)
    rangi = models.CharField(max_length=10)

def __str__(self):
    return f"{self.turi} {self.narxi} {self.rangi}"

class Davlat(models.Model):
    nomi = models.CharField(max_length=20)
    aholisi = models.IntegerField(default=10)
    poytaxt = models.CharField(max_length=20)

def __str__(self):
    return f"{self.nomi} {self.aholisi} {self.poytaxt}"

    

