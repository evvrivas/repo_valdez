from django.template.loader import get_template
from django.template import Context

from django.template import RequestContext, loader

from django.http import HttpResponse
import datetime

#from books.models import Publisher
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
#from miPagina.books.models import Book
from settings import MEDIA_URL


from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.contrib.auth.decorators import login_required



from forms import *
from datos_artetronica.models import *

from django.contrib.auth.models import User  
from django.core.mail import send_mail


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/principal")


@login_required
def entrada_producto(request):                

        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = ProductoForm(request.POST,request.FILES)   
                    if form.is_valid():
                        form.save() # Guardar los datos en la base de datos 
                        #return render_to_response('principal.html', locals() ,context_instance=RequestContext(request))
                        return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
        else:            
                       
                        form = ProductoForm()
                        username2 = request.user.id
                        form = ProductoForm(initial={'id_usuario': username2})

        
        return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))


@login_required
def entrada_mensaje(request,bandera):               

        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = MensajeForm(request.POST)  

                    if form.is_valid():

                        form.save() # Guardar los datos en la base de datos 
                        #sender = form.clean_data.get('sender', 'noreply@example.com')
                        #send_mail('Feedback from your site, topic: %s' % topic, message, sender,['administrator@example.com'])
                        #return render_to_response('principal.html', locals() ,context_instance=RequestContext(request))
                        return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
       
        else:            
                        form = MensajeForm()
                        username2 = request.user.id
                        form = MensajeForm(initial={'id_usuario': username2})

                        #form = YourForm(initial={'fieldname': somevalue})
                       # print username2
       
        if bandera=="0": 
                  

                  mensajes_anteriores=Mensaje.objects.filter(id_usuario=request.user.id).order_by("-id")    
                  
        else:
                  
                  mensajes_anteriores=Mensaje.objects.all().order_by("-id") 
    
        

        return render_to_response('mensajes.html', locals() ,context_instance=RequestContext(request))







def entrada_usuario(request): 
       
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    form = UsuarioForm(request.POST,request.FILES)   
                    if form.is_valid():

                        alias = form.cleaned_data['alias']
                        mail = form.cleaned_data['email']
                        contra = form.cleaned_data['contrasena'] 
                        first =form.cleaned_data['nombres']                       
                        last=form.cleaned_data['apellidos']

                        #sender = form.clean_data.get('sender', 'noreply@example.com')
                        #send_mail('Feedback from your site, topic: %s' % topic, message, sender,['administrator@example.com'])
                                             
                        user = User.objects.create_user(username=alias, email=mail,password=contra,first_name=first,last_name=last)
                        user.save()
                        form.save() # Guardar los datos en la base de datos  print 
                        
                        return render_to_response('confirmar.html', locals() ,context_instance=RequestContext(request))
        else:            
                        form = UsuarioForm()
       
        return render_to_response('formulario.html', locals() ,context_instance=RequestContext(request))
    



def listado_producto(request,bandera):          
    productos=Producto.objects.filter(categoria=bandera)
    return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))





    
def listado(request,bandera):

    if bandera=="usuario":     
        productos= Usuario.objects.all() 
        return render_to_response('usuarios.html', locals(),context_instance=RequestContext(request))
    
    elif bandera=="staff":     
        productos= Staff.objects.all() 
        return render_to_response('staff.html', locals(),context_instance=RequestContext(request))
    
    elif bandera=="producto":     
        productos= Producto.objects.all() 
        return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
    
    else:     
        productos= Producto.objects.all() 
        return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))
    
   

    
@login_required
def editar(request, acid):
    f = Producto.objects.get(pk=acid)    
    #message = Pedido.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST,instance=f)
        if form.is_valid():
            form.save() 
            return render_to_response('confirmar.html',locals(),context_instance=RequestContext(request))          
    else:
        form = ProductoForm(instance=f)    
        
    return render_to_response('formulario.html',locals(),context_instance=RequestContext(request))



    
      
        
import datetime
#@login_required
def pagina_principal(request):
    current_date = datetime.datetime.now()

    return render_to_response('principal.html', locals(),context_instance=RequestContext(request))

def catalogo(request, var):
	current_date = datetime.datetime.now()	
	
	return render_to_response('catalogo.html', locals(),context_instance=RequestContext(request))

def informacion(request):
	current_date = datetime.datetime.now()
	
	return render_to_response('informacion.html', locals(),context_instance=RequestContext(request))




from datos_artetronica.cart import Cart
@login_required
def add_to_cart_PCB(request, product_id,precio):
    #print request
    
    quantity= request.POST["cantidad"]
    
   
    product = Pcb.objects.get(id=product_id)  
    print  "########"
    print  quantity, product, precio

    cart = Cart(request)
    cart.add(product, precio, quantity)
    total=cart.summary()    
    

    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))


@login_required
def add_to_cart(request, product_id):

    quantity= request.POST["cant"]
    product = Producto.objects.get(id=product_id)   



    if quantity==1:
        precio=product.precio_A
    elif quantity>=2 and quantity <=5:
        precio=product.precio_B
    elif quantity>=6:
        precio=product.precio_C
    else :
        precio=product.precio_A

    print  "########"
    print  quantity, product, precio 
    cart = Cart(request)
    cart.add(product, precio, quantity)
    total=cart.summary()
    

    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))

@login_required
def remove_from_cart(request, product_id):
    product = Producto.objects.get(id=product_id)
    cart = Cart(request)
    cart.remove(product)

@login_required
def get_cart(request):
    print "getcqr" 
    cart = Cart(request)
    cart.view()
    return render_to_response('carrito.html', locals(),context_instance=RequestContext(request))

@login_required
def pedido(request):    
    cart = Cart(request)
    cart.view()    
    fecha= datetime.datetime.now()
    
    mensaje= str(fecha)+"  "+str(request.user.first_name) + "  "+str(request.user.last_name) +"  "+ str(request.user.id)+"  "+"\n"

    for item in cart:
        mensaje=mensaje+"  "+ str(item.product)+ "  "+ str(item.unit_price)+ "  "+str(item.quantity)+"  "+ str(item.total_price)+"  "+"\n"

                                
    mensaje=mensaje+"\n" 
    topic = "Pedido"   
    sender =str(request.user.email)

    print mensaje

    send_mail('Feedback from your site, topic: %s' % topic,  mensaje, sender,
    ['artetronica@gmail.com']
    )
    
    
    return render_to_response('cotizacion.html', locals(),context_instance=RequestContext(request))
 














####libreria de algun fulano que se utiliza para calcular el CRC de on byte
table = tuple()
# crc16_Init() - Initialize the CRC-16 table (crc16_Table[])
def init_table( ):
    global table

    if( (len( table) == 256) and (table[1] == 49345)):
        # print "Table already init!"
        return
   
    lst = []
    i = 0
    while( i < 256):
        data = (i << 1)
        crc = 0
        j = 8
        while( j > 0):
            data >>= 1
            if( (data ^ crc) & 0x0001):
                crc = (crc >> 1) ^ 0xA001
            else:
                crc >>= 1
            j -= 1
           
        lst.append( crc)
        # print "entry %d = %x" % ( i, table[i])
        i += 1

    table = tuple( lst)       
    return

# given a Byte, Calc a modbus style CRC-16 by look-up table
def calcByte( ch, crc):
    init_table( )
    if( type(ch) == type("c")):
        by = ord( ch)
    else:
        by = ch
    crc = (crc >> 8) ^ table[(crc ^ by) & 0xFF]
    return (crc & 0xFFFF)


###############################################################



def calcular(id_maquina):

                print "cjcjcjcjcjc"
                dato=id_maquina
                letras=""
                crc=0xffff
                for i in dato:
                     try:
                       x=eval(i)
                       crc= calcByte( x, crc)
                     except:
                       letras=letras+i
                     
                contrasena=str(crc)+letras   

                return  contrasena



@login_required
def descargar_serial_key(request):
       

        ide_de_usuario = request.user.id   
        x=ide_de_usuario-1 #sumo uno pq USER y USUARIO no es igual
        f = Usuario.objects.get(pk=x)
        cant_bonos=f.bonos
        
        if request.method == 'POST': # si el usuario est enviando el formulario con datos
                   
                   
                    if cant_bonos>0:                                
                                  
                               cant_bonos=cant_bonos-1
                               f.bonos=cant_bonos
                               f.save()

                               form = Seriales_pymblockForm(request.POST)                      

                               if form.is_valid(): 
                                    form.save()
                                                                        
                    else:
                            mensaje= "usted no tiene bonos"  

                    return render_to_response('principal.html', locals() ,context_instance=RequestContext(request))
        else:            
                        
                        form = Seriales_pymblockForm()
                        form = Seriales_pymblockForm(initial={'id_usuario': int(ide_de_usuario)})
                        print "kaka"
        
        
        contrasenas=[] 
        print "ULO"      
            
        
        seriales_keys_anteriores=Seriales_pymblock.objects.filter(id_usuario=ide_de_usuario).order_by("-id") 


            
        for i in seriales_keys_anteriores:
                 
                b = calcular(i.id_usuario_pymblock)
                a = i.id_usuario_pymblock
                contrasenas.append( (a,b) )
                                     
        return render_to_response('descargas.html', locals() ,context_instance=RequestContext(request))



@login_required
def pcb(request):

        ide_de_usuario = request.user.id    
               

        if request.method == 'POST': # si el usuario est enviando el formulario con datos
            
                    if  request.POST["cant"]:

                        form = PcbForm(request.POST)

                        if form.is_valid():
                           
                               form.save()
                               cantidad=form.cleaned_data['cantidad']
                               cantidad=form.cleaned_data['cantidad'] 
                               ancho=form.cleaned_data['ancho_cm'] 
                               largo=form.cleaned_data['largo_cm'] 
                               n_caras=form.cleaned_data['caras'] 
                               id_producto=form.cleaned_data['id_usuario']
                               p=Pcb()
                               print p.id
                               p=Pcb.objects.all()

                               for i in p:
                                  id_producto=i.id

                               #id_producto=request.POST['Id']
                               
                               if n_caras=="una_cara":
                                    n_caras=1
                               else:
                                     n_caras=2

                              
                               #precio cm2 = 0.15 ctvs
                               
                               precia=(ancho)*(largo)*n_caras

                               if cantidad<=2:
                                    precio=precia*0.20

                               elif cantidad>2 and cantidad<=4:
                                     precio=precia*0.16

                               elif cantidad>4 and cantidad<=6:
                                     precio=precia*0.14 
                              
                               elif cantidad>6 and cantidad<=20:
                                     precio=precia*0.08
                               
                               elif cantidad>21 and cantidad<=50:
                                     precio=precia*0.075
                               
                               elif cantidad>51 and cantidad<=99:
                                     precio=precia*0.07

                               elif cantidad>51 and cantidad<=99:
                                     precio=precia*0.068

                               elif cantidad>99: 
                                     precio=precia*0.066                                 
                               
                               else:  
                                    precio=precia*0.09

                        
                               total=precio*cantidad
                           
                               x=add_to_cart_PCB(request,id_producto,precio)
                            
                            
                               cart=get_cart(request)

                               return x
                    else:

                                    
                            form = PcbForm(request.POST)
                            if form.is_valid():
                               print form
                               cantidad=form.cleaned_data['cantidad'] 
                               ancho=form.cleaned_data['ancho_cm'] 
                               largo=form.cleaned_data['largo_cm'] 
                               n_caras=form.cleaned_data['caras'] 
                              
                               #precio cm2 = 0.15 ctvs
                               if n_caras=="una_cara":
                                    n_caras=1
                               else:
                                     n_caras=2
                               
                               precia=(ancho)*(largo)*n_caras

                               if cantidad<=2:
                                    precio=precia*0.20

                               elif cantidad>2 and cantidad<=4:
                                     precio=precia*0.16

                               elif cantidad>4 and cantidad<=6:
                                     precio=precia*0.14 
                              
                               elif cantidad>6 and cantidad<=20:
                                     precio=precia*0.08
                               
                               elif cantidad>21 and cantidad<=50:
                                     precio=precia*0.075
                               
                               elif cantidad>51 and cantidad<=99:
                                     precio=precia*0.07

                               elif cantidad>51 and cantidad<=99:
                                     precio=precia*0.068

                               elif cantidad>99: 
                                     precio=precia*0.066                                 
                               
                               else:  
                                    precio=precia*0.09

                        
                               total=precio*cantidad


                               return render_to_response('pcb.html', locals() ,context_instance=RequestContext(request))
        else:            
                        
                        form = PcbForm()   
                        form = PcbForm(initial={'id_usuario': ide_de_usuario})  
                        print "A"     

                                                
        return render_to_response('pcb.html', locals() ,context_instance=RequestContext(request))

