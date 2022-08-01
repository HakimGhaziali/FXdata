from django.db import models

# Create your models here.
from django.urls import reverse



class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField( max_digits=6 , decimal_places=2)


    def get_absolute_url(self):
        return reverse("book_detial", args=str(self.id))
    


