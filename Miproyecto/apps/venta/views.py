# Create your views here.
from django.shortcuts import render
from .models import venta
# Create your views here.

def index(request):
    ventas = venta.objects.all()
    datos = {'ventas':ventas}
    return render(request, "venta/index_venta.html", datos)