from django.shortcuts import render
from rest_framework import generics , permissions
from .serializers import PostSerializer
from blog.models import Post
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

class ApiView(generics.ListCreateAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ApiList(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UserList(generics.ListCreateAPIView):
    queryset= get_user_model().objects.all()
    serializer_class = UserSerializer




class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= get_user_model().objects.all()
    serializer_class = UserSerializer
