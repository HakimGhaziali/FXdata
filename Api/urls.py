from django.urls import path 
from .views import ApiView , ApiList , UserList, UserDetail


urlpatterns = [
    path('', ApiView.as_view() , name='ApiView'),
    path('<int:pk>', ApiList.as_view() , name='ApiList'),
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
]