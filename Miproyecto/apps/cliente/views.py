from django.shortcuts import render, redirect
from .models import cliente, pais
from .form import clienteForm


# Create your views here.

def index(request):
    clientes_registros = cliente.objects.all()
    contexto = {'clientes':clientes_registros}
    return render(request, "cliente/index_cliente.html", contexto)


def crear_clientes_predeterminados(request):
    from datetime import date

    #crear instancias de paises

    p1 = pais.objects.create(nombre="Argentina")
    p2 = pais.objects.create(nombre="Brasil")
    p3 = pais.objects.create(nombre="Chile")

    #crear clientes

    cliente.objects.create(nombre="Almendra", apellido="sanchez", nacimiento=date(2009, 1, 1), pais_origen_id=p1)
    cliente.objects.create(nombre="jhiordana", apellido="Gonzalez", nacimiento=date(1987, 2, 2), pais_origen_id=p2)
    cliente.objects.create(nombre="Juan", apellido="Perez", nacimiento=date(1990, 3, 1), pais_origen_id=p3)
    cliente.objects.create (nombre="giordana", apellido="dangelo", nacimiento=date(2005, 12, 1), pais_origen_id=None)

    #return render(request, "cliente/index_cliente.html")
    return redirect('cliente:index')   #funciona igual quue return render, el archivo puede cambiar de lugar que no importa

def prueba_busqueda(request):
    from datetime import date
    contexto = {}
    #busqueda por nombre que contenga "dana"
    clientes_nombre =cliente.objects.filter(nombre__contains="dana") 
    contexto ['clientes_nombre']=clientes_nombre

    #busqueda por fecha de nacimiento mayor al año 2000
    clientes_nacimiento = cliente.objects.filter(nacimiento__gte=date(2000, 1, 1))
    contexto ['clientes_nacimiento']= clientes_nacimiento

    #busqueda por cliente que no tenga pais designado
    cliente_no_pais = cliente.objects.filter(pais_origen_id=None)
    contexto['cliente_no_pais'] = cliente_no_pais
    return render(request, "cliente/resultado_busqueda.html", contexto)

def crear_cliente(request):

    if request.method == 'POST':
        form = clienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente:index')
    else: #method == 'GET'
        form = clienteForm()

    return render(request, "cliente/crear.html",{'form':form}) 
