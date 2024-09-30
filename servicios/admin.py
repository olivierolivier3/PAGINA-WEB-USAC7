from django.contrib import admin
from .models import Servicio #con el "punto" indicamos que nos vamos a mover dentro del mismo directorio hacia el archivo models


# Register your models here.

class ServicioAdmin(admin.ModelAdmin): #Creamos esta clase para poder agregar los campos "created y updated", al panel admin
    readonly_fields=('created','updated')#estos campos son de solo lectura, porque son campos que se rellenan automaticamente

admin.site.register(Servicio, ServicioAdmin) #agregamos aqui la clase "ServicioAdmin", para que aparezca en panel admin
