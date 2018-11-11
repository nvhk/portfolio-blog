from django.db import models

# Create your models here.
class Praca(models.Model):
    obrazek = models.ImageField(upload_to='obrazki/')
    podpis = models.CharField(max_length=245)
