from django.urls import path #importa path, se usa para definir rutas URL en la aplicacion

from .views import VRegistro, cerrar_sesion, logear


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ #contiene las rutas URL, y las vistas asociadas a estas urls.

    path('', VRegistro.as_view(), name='Autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name='cerrar_sesion'),

    path('logear', logear, name='logear'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)