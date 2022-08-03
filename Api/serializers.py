from rest_framework import serializers
from blog.models import Post 
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id', 'user', 'title', 'text', 'datetime_created','status')
        model = Post




class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = get_user_model()
        fields = ('id' , 'username',)