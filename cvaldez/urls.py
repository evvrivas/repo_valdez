
from django.conf.urls import patterns, url, include

from django.contrib import admin

from cvaldez.views import *
from django.conf import settings
import settings

from django.contrib.auth.views import login, logout
from django.conf.urls.static  import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',url(r'^time/$', current_datetime,name='my-view'),(r'^inicio/$', pagina_inicial),
	(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
	url(r'^admin/', include(admin.site.urls)),(r'^accounts/login/$', login),(r'^accounts/logout/$', logout),
	)
                   
urlpatterns += patterns('',
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
       'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
   url(r'^lista_de_inventario/(\d+)$',lista_de_inventario), url(r'^editar_inventario/(\d+)$',editar_inventario),
   url( r'^hacer_inventario/$', hacer_inventario),
   )

urlpatterns += patterns('',
   url(r'^lista_de_pedidos/(\d+)$',lista_de_pedidos),url(r'^editar_pedido/(\d+)$',editar_pedido),
   url( r'^hacer_pedido/$', hacer_pedido),(r'^editar_estado_del_pedido/(\d+)$',editar_estado_del_pedido),
   )

urlpatterns += patterns('',
   (r'^editar_cliente/(\d+)$',editar_cliente),url( r'^nuevo_cliente/$', nuevo_cliente),
   url( r'^lista_de_clientes/$',lista_de_clientes),
   )
#if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    #urlpatterns += patterns('',
        #(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        #'document_root': settings.MEDIA_ROOT}))
