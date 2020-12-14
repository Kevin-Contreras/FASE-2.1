from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render


def clientes(request):
  return render(request,"cliente.html")
def inicios(request):
  return render(request,"inicio.html")
def ahorro(request):
  return render(request,"crearAhorro.html")
def ventanaproveedorbasico(request):
  return render(request,"servicoProveedor.html")
def proveedor(request):
  return render(request,"pagoPlanilla.html")
def proveedores(request):
  return render(request,"basicos.html")
def trans(request):
  return render(request,"transacciones.html")
def propias(request):
  return render(request,"propias.html")
def cuentaTercero(request):
  return render(request,"terceros.html")
def menuCheques(request):
  return render(request,"menucheque.html")
def emitirCheque(request):
  return render(request,"emitir.html")
def recibirCheque(request):
  return render(request,"recibir.html")
def estados(request):
  return render(request,"estado.html")
def prestamos(request):
  return render(request,"prestamo.html")
def iniciosAhorro(request):
  return render(request,"inicioAhorro.html")
def iniciosFijo(request):
  return render(request,"plazofijo.html")
def claves(request):
  return render(request,"transaccionesclave.html")