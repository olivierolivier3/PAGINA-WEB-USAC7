from django import forms
from django.contrib.auth.forms import UserCreationForm # importamos esta libreria, porque es donde se encuentra lo necesario para Registrar usuarios
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
    
