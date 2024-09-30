from django.urls import path #importa path, se usa para definir rutas URL en la aplicacion

from . import views

urlpatterns = [ #contiene las rutas URL, y las vistas asociadas a estas urls.

    path('', views.procesar_pedido, name='procesar_pedido'),#el name se usa para referenciar el URL, en alguna otra parte del codigo o programa.
]

