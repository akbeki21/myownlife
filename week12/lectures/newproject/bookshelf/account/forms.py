from django.contrib.auth.forms import UserCreationForm

from .models import MyUser

class UserRegistrationForm(UserCreationForm):
    """Form to register user"""
    class Meta:
        model = MyUser
        fields = ('email', 'password1', 'password2')