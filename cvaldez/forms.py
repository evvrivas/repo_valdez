from datosvaldez.models import Cliente,Pedido,Inventario
from django.forms import ModelForm

from django.forms import ModelForm, Textarea


class ClienteForm(ModelForm):
	class Meta:
		model=Cliente

class PedidoForm(ModelForm):
	class Meta:
		model=Pedido
		widgets = {'precios_unitartios': Textarea(attrs={'cols': 40, 'rows': 3}),'descripcion_bordado': Textarea(attrs={'cols': 40, 'rows': 3}),'descripcion_cuellos': Textarea(attrs={'cols': 40, 'rows': 3}),}

class InventarioForm(ModelForm):
	class Meta:
		model=Inventario
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 3}),}
