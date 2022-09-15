from django.urls import path 
from .views import PostList , post_detail , PostCreateView ,PostUpdateView , PostUpdateView , PostDeleteView



urlpatterns = [
    path("", PostList.as_view() , name='post_list'),  
    path("<int:pk>", post_detail , name='post_detail'), 
    path("create", PostCreateView.as_view() , name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

