from django.shortcuts import render 
from rest_framework import viewsets , permissions
from .serializers import PostSerializer
from blog.models import Post
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


class ApiView(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(viewsets.ModelViewSet):
    queryset= get_user_model().objects.all()
    serializer_class = UserSerializer

