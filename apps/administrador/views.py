from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from apps.administrador.models import Administrador
from django.db import connection
import mysql.connector
mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="123naruto",
  database="proyecto"
)

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
        return render(request,"menuAdmin.html",{"Dato":dato })
      else:
       print("")
  else:
    return render(request,"administrador.html")
  return render(request,"administrador.html", {"contra":"LA CONTRASEÑA O USUARIO ES INCORRECTO"})
# Create your views here.
