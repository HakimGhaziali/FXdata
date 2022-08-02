from django.urls import path 
from .views import ApiView , ApiList



urlpatterns = [
    path('', ApiView.as_view() , name='ApiView'),
    path('<int:pk>', ApiList.as_view() , name='ApiList'),
]