from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def saludar (request):
  nombre = "KEVIN"
  return render(request,"index.html",{"nombre_persona":nombre})
def administrador(request):
  return render(request,"administrador.html")
def seleccionarCliente(request):
  return render(request,"seleccionarCliente.html") 
def crearPersona(request):
  return render(request,"persona.html")
def crearEmpresa (request):
  return render(request,"empresa.html")
def clientes(request):
  return render(request,"cliente.html")