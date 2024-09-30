from django.urls import path #importa path, se usa para definir rutas URL en la aplicacion
from . import views


urlpatterns = [ #contiene las rutas URL, y las vistas asociadas a estas urls.

    path('', views.blog, name='Blog'), #el espacio que queda vacio entre comillas, es el apuntador de la raiz

    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'), #<categoria_id> es el parametro de la bd, que vamos a usar como identificador

]