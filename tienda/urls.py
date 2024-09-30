from django.urls import path #importa path, se usa para definir rutas URL en la aplicacion

from . import views


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ #contiene las rutas URL, y las vistas asociadas a estas urls.

    path('', views.tienda, name='Tienda'),#el name se usa para referenciar el URL, en alguna otra parte del codigo o programa.
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)