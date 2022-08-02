from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from blog.models import Post

class ApiView(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ApiList(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer