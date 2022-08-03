from django.shortcuts import render
from rest_framework import generics , permissions
from .serializers import PostSerializer
from blog.models import Post

class ApiView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ApiList(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer