from django.db import models

# Create your models here.
class Blog(models.Model):
    tytul = models.CharField(max_length=100)
    data = models.DateField(auto_now=True)
    tekst = models.TextField()
    obrazekbloga = models.ImageField(upload_to='obrazki/')
