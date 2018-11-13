from django.db import models

# Create your models here.
class Blog(models.Model):
    tytul = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now_add=False)
    tekst = models.TextField()
    obrazekbloga = models.ImageField(upload_to='obrazki/')

    def skrotTekstu(self):
        return self.tekst[:255]

    def __str__(self):
        return self.tytul
