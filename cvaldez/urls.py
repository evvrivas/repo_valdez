
from django.conf.urls import patterns,url,include

from django.contrib import admin


from django.conf import settings
import settings

from django.contrib.auth.views import login, logout

from django.conf.urls.static  import static 


from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from cvaldez.views import *




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'artetronica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',include(admin.site.urls)),
    (r'^accounts/login/$', login,{'template_name': 'login.html'}),
    (r'^accounts/logout/$', logout),
)

#r'^admin/', include(admin.site.urls)


urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += patterns('',	(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.STATIC_ROOT}))
urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  settings.MEDIA_ROOT}))



urlpatterns += patterns('',(r'^principal/$', pagina_principal),(r'^catalogo/(\d+)$', catalogo),(r'^informacion/$', informacion)) + staticfiles_urlpatterns()

urlpatterns += patterns('',(r'^listado/([a-z]+)$', listado),(r'^pedido/$', pedido),(r'^editar/(\d+)/$', editar),)
urlpatterns += patterns('',(r'^entrada_usuario/$', entrada_usuario),(r'^entrada_mensaje/(\d+)$', entrada_mensaje),(r'^entrada_producto/$', entrada_producto),)

urlpatterns += patterns('',(r'^listado_producto/([a-z]+)$', listado_producto),(r'^pcb/$', pcb))

urlpatterns += patterns('',(r'^add_to_cart/(\d+)/$', add_to_cart),(r'^descargas/$',descargar_serial_key),(r'^get_cart/$', get_cart),)










