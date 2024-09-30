from django.contrib import admin

from .models import Pedido, LineaPedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    list_display=("user","created_at")

class LineaPedidoAdmin(admin.ModelAdmin):
    list_display=("user","producto","pedido","cantidad","created_at")
     


admin.site.register([Pedido],PedidoAdmin)

admin.site.register([LineaPedido], LineaPedidoAdmin)
