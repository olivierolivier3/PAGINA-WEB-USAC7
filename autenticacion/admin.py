from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email','is_superuser')  # Agrega los campos que deseas mostrar en la lista

admin.site.register(User, UserAdmin)