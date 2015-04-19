from django.template.loader import get_template
from django.template import Context

from django.template import RequestContext, loader

from django.http import HttpResponse
import datetime

#from books.models import Publisher
from django.shortcuts import render_to_response
#from miPagina.books.models import Book
from settings import MEDIA_URL


from django.contrib import auth
from django.core.files.uploadedfile import SimpleUploadedFile 
from django.contrib.auth.decorators import login_required
from datosvaldez.models import Pedido,Cliente,Inventario
from forms import PedidoForm,ClienteForm,InventarioForm


def current_datetime(request):    
    now = str(datetime.datetime.now())+" <p>hola mundo</p>"
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def pagina_inicial(request):    
    return render_to_response('inicio.txt', {'media_url':MEDIA_URL})



def nuevo_cliente(request):
    if request.method == 'POST': # si el usuario est enviando el formulario con datos
        form = ClienteForm(request.POST) # Bound form
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos
 
            return render_to_response('gracias.txt')
    else:
        form = ClienteForm() # Unbound form
 
    return render_to_response('nuevo_cliente.txt', {'form': form},context_instance=RequestContext(request))

def lista_de_clientes(request):
    #pedido=Pedido.objects.order_by("fecha_de_entrega")
    # muestra todos los pedidos
    clientes = Cliente.objects.all().order_by("nombre")    
    
    return render_to_response('lista_de_cliente.txt', {'clientes': clientes,'media_url':MEDIA_URL})

def editar_cliente(request, acid):
    f = Cliente.objects.get(pk=acid)    
    #message = Pedido.objects.get(pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST,instance=f)
        if form.is_valid():
            form.save() 
            return render_to_response('gracias.txt')          
    else:
        form = ClienteForm(instance=f)    
        
    return render_to_response('editar_cliente.txt', {'form': form},context_instance=RequestContext(request))











#@login_required
def hacer_pedido(request):
    if request.method == 'POST': # si el usuario est enviando el formulario con datos
        form = PedidoForm(request.POST,request.FILES) # Bound form
        if form.is_valid():
            form.save()
            
            return render_to_response('gracias.txt')
    else:
        form = PedidoForm() # Unbound form
 
    return render_to_response('hacer_un_pedido.txt', {'form': form},context_instance=RequestContext(request))

def lista_de_pedidos(request,a):
    #pedido=Pedido.objects.order_by("fecha_de_entrega")
    if a=="0":  # muestra todos los pedidos
       pedido = Pedido.objects.all().order_by("-fecha_de_entrega") 
    elif a=="1":   
       pedido = Pedido.objects.filter(estado_del_pedido="No_se_ha_iniciado").order_by("-fecha_de_entrega")
    elif a=="2":   
       pedido = Pedido.objects.filter(estado_del_pedido="En_corte").order_by("-fecha_de_entrega")
    elif a=="3":   
       pedido = Pedido.objects.filter(estado_del_pedido="Piezas_en_serigrafia").order_by("-fecha_de_entrega")
    elif a=="4":   
       pedido = Pedido.objects.filter(estado_del_pedido="Prendas_en_serigrafia").order_by("-fecha_de_entrega")
    elif a=="5":   
       pedido = Pedido.objects.filter(estado_del_pedido="En_confeccion").order_by("-fecha_de_entrega")
    elif a=="6":   
       pedido = Pedido.objects.filter(estado_del_pedido="Bordando_piezas").order_by("-fecha_de_entrega")
    elif a=="7":   
       pedido = Pedido.objects.filter(estado_del_pedido="Bordando_Terminados").order_by("-fecha_de_entrega")
    elif a=="8":   
       pedido = Pedido.objects.filter(estado_del_pedido="Terminado").order_by("-fecha_de_entrega")
    elif a=="9":   
       pedido = Pedido.objects.filter(estado_del_pedido="Terminado_empacado").order_by("-fecha_de_entrega")
    elif a=="10":   
       pedido = Pedido.objects.filter(estado_del_pedido="Entregado").order_by("-fecha_de_entrega")
    elif a=="11":   
       pedido = Pedido.objects.filter(estado_del_pedido="Pedido_inconsistente").order_by("-fecha_de_entrega")
    else:
       pedido = Pedido.objects.all()
    
    return render_to_response('lista_de_pedidos.txt', {'pedido': pedido,'media_url':MEDIA_URL})
  
def editar_pedido(request, acid):
    f = Pedido.objects.get(pk=acid)
    #message = Pedido.objects.get(pk=id)
    if request.method == 'POST':
        form = PedidoForm(request.POST,request.FILES,instance=f)
        if form.is_valid():
            form.save() 
            return render_to_response('gracias.txt')          
    else:
        form = PedidoForm(instance=f)
       
    return render_to_response('editar_pedido.txt', {'form': form},context_instance=RequestContext(request))

def editar_estado_del_pedido(request, acid):
    f = Pedido.objects.get(pk=acid)
    
    #message = Pedido.objects.get(pk=id)
    if request.method == 'POST':
        form = PedidoForm(request.POST,request.FILES,instance=f)
        if form.is_valid():
            form.save() 
            return render_to_response('gracias.txt')          
    else:
        form = PedidoForm(instance=f)    
        
    return render_to_response('editar_pedido.txt', {'form': form},context_instance=RequestContext(request))





def hacer_inventario(request):
    if request.method == 'POST': # si el usuario est enviando el formulario con datos
        form = InventarioForm(request.POST,request.FILES) # Bound form
        if form.is_valid():
            form.save()
            
            return render_to_response('gracias.txt')
    else:
        form = InventarioForm() # Unbound form
 
    return render_to_response('hacer_un_inventario.txt', {'form': form},context_instance=RequestContext(request))
def lista_de_inventario(request,a):
    #pedido=Pedido.objects.order_by("fecha_de_entrega")
    if a=="0":  # muestra todos los pedidos
       inventario = Inventario.objects.all().order_by("nombre") 
    elif a=="1":   
       inventario = Inventario.objects.all().order_by("lugar") 
         
    else:
       inventario = Inventario.objects.all()    
    
    return render_to_response('lista_de_inventario.txt', {'inventario': inventario,'media_url':MEDIA_URL})


def editar_inventario(request, acid):
    f = Inventario.objects.get(pk=acid)
    #message = Pedido.objects.get(pk=id)
    if request.method == 'POST':
        form = InventarioForm(request.POST,request.FILES,instance=f)
        if form.is_valid():
            form.save() 
            return render_to_response('gracias.txt')          
    else:
        form = InventarioForm(instance=f)
       
    return render_to_response('editar_inventario.txt', {'form': form},context_instance=RequestContext(request))


"""
django view methods to interact with the dropbox api
"""


from dropbox import client, session
from dropbox.rest import ErrorResponse
from oauth.oauth import OAuthToken

from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from models import DropboxExtra


DROPBOX_REQUEST_SESSION_KEY = 'dropbox_request_token3' # random temp storage name

def _saveUserToken(user, token):
    try:
        d = user.django_dropbox
    except:
        d = DropboxExtra()
        d.user = user
    d.dropbox_token = token
    d.save()

def _dropboxConnect(request,sess):
    request_token = sess.obtain_request_token()
    request.session[DROPBOX_REQUEST_SESSION_KEY] = request_token
    url = sess.build_authorize_url(request_token,request.build_absolute_uri())
    return HttpResponseRedirect(url)


def dropbox_user_required(funk):
    @login_required
    def _dropbox_wrap(request, *args, **kwargs):
        _keys = settings.DROPBOX_SETTINGS
        sess = session.DropboxSession(_keys['app_key'], _keys['app_secret'],_keys['type'])
        try:
            if request.session.has_key(DROPBOX_REQUEST_SESSION_KEY):
                sess.token = sess.obtain_access_token(request.session.pop(DROPBOX_REQUEST_SESSION_KEY))
                _saveUserToken( request.user, sess.token )
            else:
                token = request.user.django_dropbox.dropbox_token
                sess.token =  OAuthToken.from_string(token)
            c = client.DropboxClient(sess)
        except ObjectDoesNotExist:
            return _dropboxConnect(request, sess)
        try:
            return funk(request, *args, dropbox_client=c, **kwargs)
        except ErrorResponse, e:
            if e.status == 401:
                _dropboxConnect(request, sess)# re authentication needed
            else:
                raise e # let django log the exception that the usier did not handle

    return _dropbox_wrap
