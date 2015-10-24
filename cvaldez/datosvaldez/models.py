from django.db import models
from django.contrib.admin.widgets import AdminDateWidget 
from datetime import datetime 

from django.contrib.auth.models import User


CATEGORIA = (
   ('tarjeta', 'tarjeta'),
   ('kits', 'kits'),
   ('Software', 'Software'),
   ('shields', 'shields'),
   ('elementos', 'elementos'),
   ('proyecto', 'proyecto'),
   ('sensores', 'sensores'),
   ('impreso', 'impreso'),

   )

TIPO_USUARIO = (
   ('vendedor', 'vendedor'),
   ('comprador', 'comprador'),
   
   )

OCUPACION = (
   ('estudiante_universitario', 'estudiante_universitario'),
   ('estudiante_bachillerato', 'estudiante_bachillerato'),
   ('estudiante_basica', 'estudiante_basica'),
   ('profesional', 'profesional'),
   ('aficionado', 'aficionado'),
   
   )
CARAS = (  ('una_cara', 'una_cara'), ('doble_cara', 'doble_cara'),  )

class Producto(models.Model):
      id_usuario=models.IntegerField()
      categoria=models.CharField(max_length=30,choices=CATEGORIA)
      cantidad         =  models.DecimalField(max_digits=15,decimal_places=0,default=0)
      nombre           =  models.CharField(max_length=30)
      descripcion = models.TextField()
      imagen1      = models.ImageField(upload_to='tmp')
      imagen2      = models.ImageField(upload_to='tmp',blank=True)
      imagen3      = models.ImageField(upload_to='tmp',blank=True)
      manual      =      models.URLField(blank=True)
      video       =       models.URLField(blank=True)
      software     =      models.URLField(blank=True)
      precio_A  = models.FloatField(blank=True,null= True	)
      precio_B  = models.FloatField(blank=True,null= True)
      precio_C = models.FloatField(blank=True,null= True)
      fecha_ingreso = models.DateField(default=datetime.now)
      def __str__(self):
        return  self.nombre
      class Admin:
        list_display = ('categoria', 'cantidad', 'nombre','precio_A')
        #ordering = ('fecha_ingreso')
        #search_fields = ('nombre')#




class Pcb(models.Model):
      id_usuario=models.IntegerField()
      caras=models.CharField(max_length=30,choices=CARAS)
      cantidad =  models.IntegerField()
      largo_cm=models.IntegerField()
      ancho_cm=models.IntegerField()      
      fecha_ingreso = models.DateField(default=datetime.now)
      def __str__(self):
        return  self.caras
      class Admin:
        list_display = ('caras', 'cantidad', 'precio_A')
        #ordering = ('fecha_ingreso')
        #search_fields = ('nombre')#

class Entrada(models.Model):         
        entrada=models.IntegerField()        
              
        
class Staff(models.Model):
        imagen1=models.ImageField(upload_to='tmp')
        imagen2      = models.ImageField(upload_to='tmp',blank=True)
        imagen3      = models.ImageField(upload_to='tmp',blank=True)       
        nombres=models.CharField(max_length=30)
        apellidos=models.CharField(max_length=30)
        alias=models.CharField(max_length=30)
        descripcion = models.TextField()
        fecha_ingreso=models.DateField(default=datetime.now)
        #producto = models.ManyToManyField(Producto)
        def __str__(self):
          return  self.nombres
        class Admin:
          list_display = ('apellidos', 'nombres')
          ordering = ('fecha_ingreso')
          search_fields = ('nombres')



class Usuario(models.Model):
        imagen1=models.ImageField(upload_to='tmp')
        #categoria=models.CharField(max_length=30,choices=TIPO_USUARIO)
        nombres=models.CharField(max_length=30)
        apellidos=models.CharField(max_length=30)
        alias=models.CharField(max_length=30)
        email = models.EmailField()
        contrasena=models.CharField(max_length=30)
        direccion_exacta=models.CharField(max_length=60)
        ciudad_pais=models.CharField(max_length=30)
        ocupacion=models.CharField(max_length=30,choices=OCUPACION)
        fecha_ingreso=models.DateField(default=datetime.now)
        bonos=models.IntegerField(default=2)
        #producto = models.ManyToManyField(Producto)
        def __str__(self):
	    	  return  self.nombres
        class Admin:
  	    	list_display = ('categoria', 'nombre')
  	    	ordering = ('fecha_ingreso')
  	    	search_fields = ('nombre')

	


class Mensaje(models.Model):
  id_usuario=models.IntegerField(blank=True,)
  mensaje = models.TextField() 
  respuesta = models.TextField(blank=True)
  fecha= models.DateField(default=datetime.now,blank=True,)
  def __str__(self):
    return  self.mensaje
  class Admin:
    pass

class Seriales_pymblock(models.Model):
  id_usuario=models.IntegerField()
  id_usuario_pymblock = models.CharField(max_length=30)
  fecha= models.DateField(default=datetime.now)
  def __str__(self):
    return  self.id_usuario
  class Admin:
    pass


from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name=_('creation date'))
    checked_out = models.BooleanField(default=False, verbose_name=_('checked out'))

    class Meta:
        verbose_name = _('cart')
        verbose_name_plural = _('carts')
        ordering = ('-creation_date',)

    def __unicode__(self):
        return unicode(self.creation_date)

class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['content_type'] = ContentType.objects.get_for_model(type(kwargs['product']))
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)

class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name=_('cart'))
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    unit_price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=_('unit price'))
    # product as generic relation
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()

    objects = ItemManager()

    class Meta:
        verbose_name = _('item')
        verbose_name_plural = _('items')
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)