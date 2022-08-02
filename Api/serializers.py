from rest_framework import serializers
from blog.models import Post 


class PostSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('id', 'user', 'title', 'text', 'datetime_created','status')
        model = Post