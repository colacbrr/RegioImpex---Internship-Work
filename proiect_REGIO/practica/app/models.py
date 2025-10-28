# app/models.py
from django.db import models
from users.models import CustomUser  # Importă modelul CustomUser din users

class Tipuri(models.Model):
    tip = models.CharField(max_length=255)

    def __str__(self):
        return self.tip

class MotiveBypass(models.Model):
    motiv = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.motiv

class Transportatori(models.Model):
    nume = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.nume

class Soferi(models.Model):
    nume = models.CharField(max_length=255)
    companie = models.ForeignKey(Transportatori, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nume

class Cisterne(models.Model):
    nr_cisterna = models.CharField(max_length=255, unique=True)
    companie = models.ForeignKey(Transportatori, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nr_cisterna

class TipStatie(models.Model):
    tip_statie = models.CharField(max_length=255)
    def __str__(self):
        return self.tip_statie

class Client(models.Model):
    nume = models.CharField(max_length=255)
    tip_statie = models.ForeignKey(TipStatie, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.nume

class Particular(models.Model):
    nume = models.CharField(max_length=255)
    tip_statie = models.ForeignKey(TipStatie, on_delete=models.CASCADE, default=2)
    def __str__(self):
        return self.nume
class Depozit(models.Model):
    nume = models.CharField(max_length=255)
    tip_statie = models.ForeignKey(TipStatie, on_delete=models.CASCADE, default=4)
    def __str__(self):
        return self.nume
class Test(models.Model):
    nume = models.CharField(max_length=255)
    tip_statie = models.ForeignKey(TipStatie, on_delete=models.CASCADE, default=3)
    def __str__(self):
        return self.nume
class Statie(models.Model):
    nume = models.CharField(max_length=255)
    tip_statie = models.ForeignKey(TipStatie, on_delete=models.CASCADE, default=5)
    cod_statie = models.CharField(max_length=255, blank=True, null=True)
    info_statie = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.nume

class Bypass(models.Model):
    motiv = models.ForeignKey(MotiveBypass, on_delete=models.CASCADE)
    sofer = models.ForeignKey(Soferi, on_delete=models.CASCADE)
    transportator = models.ForeignKey(Transportatori, on_delete=models.CASCADE)
    cisterna = models.ForeignKey(Cisterne, on_delete=models.CASCADE)
    tip = models.ForeignKey(Tipuri, on_delete=models.CASCADE)
    tip_statie = models.ForeignKey(TipStatie, on_delete=models.CASCADE)
    utilizator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Folosește CustomUser din users
    observatii = models.CharField(max_length=300)
    


