from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from django.contrib.auth import get_user_model

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        
        model = CustomUser
        fields = ('email', 'username' ,)


class CustomUserChangeForm(UserChangeForm):

    class Meta:

        model = CustomUser
        fields = ('email','username',)