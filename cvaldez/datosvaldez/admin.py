from django.contrib import admin

# Register your models here.
from cvaldez.datosvaldez.models import Cliente,Pedido,Inventario

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Inventario)



from cvaldez.forms import PedidoForm
class RulesAdmin(admin.ModelAdmin):
    form = PedidoForm

from cvaldez.forms import InventarioForm
class RulesAdmin(admin.ModelAdmin):
    form = InventarioForm

