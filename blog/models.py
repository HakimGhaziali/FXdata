from django.urls import reverse
from django.db import models
from django.contrib.auth import get_user_model


session = (
    ('asi', 'asia'),
    ('eur', 'europe'),
    ('us','usa'),
    )


STATUS_POST = (
        ('news', 'news'),
        ('article', 'article'),
    ) 


class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name='user')
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)
    upload = models.ImageField(upload_to ='upload/' , blank=True)
    session = models.CharField(choices=session, max_length=10)
    type = models.CharField(choices=STATUS_POST, max_length=10)



    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.pk])




class Comment(models.Model):

    content = models.TextField()
    post = models.ForeignKey(Post , on_delete=models.CASCADE , related_name='comments')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name='user_comment')


    def __str__(self):

        return self.content






Currency = (
    ('usd', 'usd'),
    ('eur', 'eur'),
    ('gbp','gbp'),
    ('aud','aud'),
    ('nzd','nzd'),
    ('cad','cad'),
    ('jpy','jpy'),
    ('cny','cny')
    )



class EconomicCalender(models.Model):

    Date = models.DateTimeField()
    currency = models.CharField(choices=Currency, max_length=10)
    name= models.CharField(max_length=200)
    detail = models.TextField()
    actual = models.CharField(max_length=100)
    previous = models.CharField(max_length=100)
    actual = models.CharField(max_length=100)
    
