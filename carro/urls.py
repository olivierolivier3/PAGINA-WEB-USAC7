from django.urls import path #importa path, se usa para definir rutas URL en la aplicacion

from . import views

app_name="carro"


urlpatterns = [ #contiene las rutas URL, y las vistas asociadas a estas urls.

    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregar"),

    path("eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminar"),
    
    path("restar/<int:producto_id>/", views.restar_producto, name="restar"),
    
    path("limpiar/", views.limpiar_carro, name="limpiar"),
]

