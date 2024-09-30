from django import forms
from django.contrib.auth.forms import UserCreationForm # importamos esta libreria, porque es donde se encuentra lo necesario para Registrar usuarios
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','picture']
    
