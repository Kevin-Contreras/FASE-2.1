from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
from apps.administrador.models import Administrador,Clienteempresa,Persona
from django.db import connection
import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123naruto",
  database="proyecto"
)
sesion =[]
sesion2=[]
def nose(request):
 # mycursor = mydb.cursor()
  #sql = "INSERT INTO administrador (usuario, contrasenia) VALUES (%s, %s)"
  #val = ("John", "Hi")
 # mycursor.execute(sql, val)
 # mydb.commit()
  datos = Administrador.objects.all()
  if request.method == "POST":
    for dato in datos:
      print(dato.contrasenia)
      if request.POST['password'] == dato.contrasenia and request.POST['usuario'] == dato.usuario:
        sesion.append(dato.usuario)
        return render(request,"menuAdmin.html",{"Dato":dato })

      else:
       print("")
  else:
    return render(request,"administrador.html")
  return render(request,"administrador.html", {"contra":"LA CONTRASEÑA O USUARIO ES INCORRECTO"})
# Create your views here.
def menuVista (request):
 
  return render(request,"clienteCrear.html", {"sesi":sesion[0]})



def clientesCreacion(request):
 
  if request.method == "POST":
    mycursor = mydb.cursor()
    sql = "INSERT INTO persona (usuarioPersona,cui,nit,nombre,fecha,contraPersonal,adminn,tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (request.POST["usuarioPersona"], request.POST["cuiPersona"], request.POST["nitPersona"], request.POST["nombrePersona"], request.POST["fecha"], request.POST["contraPersona"], sesion[0], "PERSONAL")
    mycursor.execute(sql, val)
    mydb.commit()
    return render(request,"creacionCliente.html",{"nota":"EL USUARIO HA SIDO CREADO CON EXITO"})
  else:
    return render(request,"creacionCliente.html")



def empresaCreada(request):
  if request.method == "POST":
    mycursor = mydb.cursor()
    sql = "INSERT INTO clienteempresa (usuarioEmpresa,tipoEmpresa,nombreEmpresa,nombreComercial,representante,cui,contraEmpresarial,adminn,tipo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (request.POST["usuarioEmpresa"],request.POST["tipoEmpresa"], request.POST["nombreEmpresa"], request.POST["nombreComercial"], request.POST["nombreLegal"], request.POST["cuiEmpresa"],request.POST["contraEmpresa"], sesion[0], "EMPRESA")
    mycursor.execute(sql, val)
    mydb.commit()
    return render(request,"crearEmpresa.html",{"nota":"EL USUARIO HA SIDO CREADO CON EXITO"})
  else:
    return render(request,"crearEmpresa.html")
def cuenta (request):
  if(request.method == "POST"):
    print(request.POST["tipoUsuario"])
    sesion2.append(request.POST["tipoUsuario"])
    sesion2[0]=request.POST["tipoUsuario"]
    return redirect('/cuenta2/')
  else:
    return render(request,"vistaOpcion.html")

def cuenta2 (request):
  datos = Persona.objects.all()
  empresas = Clienteempresa.objects.all()
  print(sesion2[0])
  if(sesion2[0]=="PERSONAL"):
      return render(request,"cuenta.html",{"persona":datos})
  elif(sesion2[0]=="EMPRESARIAL"):
       return render(request,"cuenta.html",{"persona":empresas})
   
      