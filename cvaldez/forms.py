from datos_artetronica.models import *

from django.forms import ModelForm, Textarea

class ProductoForm(ModelForm):
	class Meta:
		model= Producto
		widgets = {'descripcion': Textarea(attrs={'cols': 40, 'rows': 3}),}

class UsuarioForm(ModelForm):
	class Meta:
		model= Usuario
		
class MensajeForm(ModelForm):
	class Meta:
		model=Mensaje
		widgets = {'mensaje': Textarea(attrs={'cols': 30, 'rows': 3}),'respuesta': Textarea(attrs={'cols': 30, 'rows': 3}),}


class Seriales_pymblockForm(ModelForm):
	class Meta:
		model=Seriales_pymblock

class StaffForm(ModelForm):
	class Meta:
		model=Staff

class PcbForm(ModelForm):
	class Meta:
		model=Pcb

		
		

