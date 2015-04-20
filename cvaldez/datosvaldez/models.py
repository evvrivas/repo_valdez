from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime

# Create your models here.
# Create your models here.
PLAZO_DE_ENTREGA= (
   ('0','0'),
   ('1','1'),
   
   
)
#PLAZO_DE_ENTREGA= (
 #  ('Hoy mismo', 0),
  # ('Un dias', 1),
   #('Dos dias', 2),
   #('Tres dias', 3),
   #('Cuatro dias', 4),
   #('Cinco dias', 5),
   #('Seis dias', 6),
   #('Ocho dias', 8),
   #('Diez dias', 10),
   #('Doce dias', 12),
   #('Quince dias', 15),
   #('Diesisiete dias', 17),
   
#)

HORAS_DE_ENTREGA = (
   ('9am', '9am'),
   ('10am', '10am'),
   ('11am', '11am'),
   ('12am', '12am'),
   ('2pm', '2pm'),
   ('3pm', '3pm'),
   ('4pm', '4pm'),
   ('5pm', '5pm'),
)

ESTADO_DE_CUENTA = (
   ('Abono_inicial', 'Abono_inicial'),
   ('Pendiente_de_pago', 'Pendiente_de_pago'),
   ('Cancelado', 'Cancelado'),
)

ESTADO_PEDIDO = (
   ('No_se_ha_iniciado', 'No_se_ha_iniciado'), 
   ('En_Corte', 'En_corte'), 
   ('Piezas_en_serigrafia ', 'Piezas_en_serigrafia'), 
   ('Prendas_en_serigrafia ', 'Prendas_en_serigrafia'), 
   ('En_confeccion', 'En_confeccion'),
   ('Bordando_piezas', 'Bordando_piezas'),
   ('Bordando_Terminados', 'Bordando_Terminados'),
   ('Terminado', 'Terminado'),
   ('Terminado_empacado ', 'Terminado_empacado'),
   ('Entregado', 'Entregado'),
   ('Pedido_inconsistente', 'Pedido_inconsistente'),
   ('Pedido_anulado', 'Pedido_anulado'),
)

class Cliente(models.Model): 
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(blank=True,max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.EmailField(blank=True,max_length=50)
    registro = models.CharField(blank=True,max_length=50)
    giro = models.CharField(blank=True,max_length=50)
    dui = models.CharField(blank=True,max_length=50)
    nit = models.CharField(blank=True,max_length=50)
    def __str__(self):
        return self.nombre
    class Admin:
        pass    


class Pedido(models.Model): 
    cliente = models.ForeignKey(Cliente)   
    descripcion = models.TextField() 
    precios_unitartios = models.TextField()
    imagen1_de_pedido= models.ImageField(blank=True,upload_to='tmp')
    imagen2_de_pedido= models.ImageField(blank=True,upload_to='tmp')
    descripcion_bordado  = models.TextField(blank=True)
    imagen_de_bordado= models.ImageField(blank=True,upload_to='tmp')
    descripcion_cuellos  = models.TextField(blank=True)
    fecha_de_orden  = models.DateTimeField( default=datetime.now) 
    fecha_de_entrega = models.DateField('fecha entrega mes/dia/anho')     
    hora_de_entrega  = models.CharField(max_length=10,choices=HORAS_DE_ENTREGA)
    total  =models.DecimalField(max_digits=15,decimal_places=0,default=0)
    anticipo = models.DecimalField(max_digits=15,decimal_places=0,default=0)
    estado_de_la_cuenta = models.CharField(max_length=30,choices=ESTADO_DE_CUENTA)   
    estado_del_pedido   = models.CharField(max_length=30,choices=ESTADO_PEDIDO)
   
    def __str__(self):
        return  self.estado_del_pedido
    class Admin:
        pass

LOCALIZACION = (
   ('Local_los_pinitos', 'Local_los_pinitos'),
   ('Taller_la_laguna', 'Taller_la_laguna'),
   ('Taller_san_antonio','Taller_san_antonio'),
   )



class Inventario(models.Model):     
    lugar   = models.CharField(max_length=30,choices=LOCALIZACION)
    nombre   = models.CharField(max_length=30)
    descripcion = models.TextField() 
    tallas = models.CharField(max_length=30)
    precios_unitartios = models.CharField(max_length=30,) 
    imagen1_de_pedido= models.ImageField(upload_to='inventario') 
   
    fecha_de_inventario  = models.DateTimeField( default=datetime.now) 
    cantidad = models.DecimalField(max_digits=15,decimal_places=0,default=0)
    
    def __str__(self):
        return   self.nombre
   
    class Admin:
        pass


