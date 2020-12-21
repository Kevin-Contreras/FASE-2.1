# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    usuario = models.CharField(primary_key=True, max_length=40)
    contrasenia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'administrador'
        
class Clienteempresa(models.Model):
    usuarioempresa = models.CharField(db_column='usuarioEmpresa', primary_key=True, max_length=40)  # Field name made lowercase.
    tipoempresa = models.CharField(db_column='tipoEmpresa', max_length=40)  # Field name made lowercase.
    nombreempresa = models.CharField(db_column='nombreEmpresa', max_length=50)  # Field name made lowercase.
    nombrecomercial = models.CharField(db_column='nombreComercial', max_length=50)  # Field name made lowercase.
    representante = models.CharField(max_length=20)
    cui = models.CharField(max_length=20)
    contraempresarial = models.CharField(db_column='contraEmpresarial', max_length=40)  # Field name made lowercase.
    adminn = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='adminn')
    tipo = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'clienteempresa'

class Persona(models.Model):
    usuariopersona = models.CharField(db_column='usuarioPersona', primary_key=True, max_length=40)  # Field name made lowercase.
    cui = models.CharField(max_length=40)
    nit = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    fecha = models.CharField(max_length=20)
    contrapersonal = models.CharField(db_column='contraPersonal', max_length=20)  # Field name made lowercase.
    adminn = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='adminn')
    tipo = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'persona'
# Create your models here.
