from django.contrib import admin

# Register your models here.
#Pedidos, Producto, usuario, Mesaje, Cart, ItemManager, Item
#from django.contrib import admin

#from .models import UserProfile




from artetronica.datos_artetronica.models import *

#admin.site.register(UserProfile)
admin.site.register(Usuario)
#admin.site.register(Pedidos)
admin.site.register(Producto)
admin.site.register(Mensaje)
#admin.site.register(Respuesta)
admin.site.register(Cart)
admin.site.register(Staff)
admin.site.register(Pcb)
admin.site.register(Seriales_pymblock)

#admin.site.register(ItemManager)
#admin.site.register(Item)



from artetronica.forms import *

#class RulesAdmin(admin.ModelAdmin):
#    form = PedidoForm


class RulesAdmin(admin.ModelAdmin):
    form = UsuarioForm


class RulesAdmin(admin.ModelAdmin):
    form = ProductoForm


class RulesAdmin(admin.ModelAdmin):
    form = MensajeForm

class RulesAdmin(admin.ModelAdmin):
    form = Seriales_pymblockForm

class RulesAdmin(admin.ModelAdmin):
    form = StaffForm

class RulesAdmin(admin.ModelAdmin):
    form = PcbForm

class RulesAdmin(admin.ModelAdmin):
    form = Seriales_pymblockForm

	
		

#class RulesAdmin(admin.ModelAdmin):
#    form = CartForm


#class RulesAdmin(admin.ModelAdmin):
#    form = ItemManagerForm

#class RulesAdmin(admin.ModelAdmin):
#    form = ItemForm

