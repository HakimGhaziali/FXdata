from django.db import models

# Create your models here.
from django.urls import reverse
from django.contrib.auth import get_user_model


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField( max_digits=6 , decimal_places=2)


    def get_absolute_url(self):
        return reverse("book_detial", args=str(self.id))
    



class Review(models.Model):

    content = models.TextField()
    author = models.ForeignKey(get_user_model() , on_delete= models.CASCADE, related_name='reviews')
    Book= models.ForeignKey(Book , related_name ='reviews' , on_delete= models.CASCADE)


    def __str__(self):

        return self.content
