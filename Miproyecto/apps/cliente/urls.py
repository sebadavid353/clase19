from django.urls import path

from .views import index , crear_clientes_predeterminados,prueba_busqueda, crear_cliente        #visualizacion del archivo index
app_name = 'cliente'
 
urlpatterns = [
    path("", index , name= 'index'),
    path('crear_clientes_predeterminados', crear_clientes_predeterminados , name= 'crear_clientes'),
    path('prueba_buscqueda/', prueba_busqueda , name='prueba_busqueda'),
    path('crear/',crear_cliente, name='crear'),
   ]