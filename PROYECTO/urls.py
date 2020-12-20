from django.urls import path
from PROYECTO.views import clientes,inicios,ahorro,ventanaproveedorbasico,proveedor,proveedores,iniciosAhorro,iniciosFijo
from PROYECTO.views import trans,propias,cuentaTercero,menuCheques,emitirCheque,recibirCheque,estados,prestamos,claves
from apps.administrador.views import nose;
urlpatterns = [
    
    path('',clientes),
    path('inicio',inicios),
    path('inicioahorro',iniciosAhorro),
    path('inicioplazo',iniciosFijo),
    path('inicio/crear_ahorro',ahorro),
    path('inicio/pagos',ventanaproveedorbasico),
    path('inicio/pagos/proveedorEmpleado',proveedor),
    path('inicio/pagos/basico',proveedores),
    path('inicio/menu',trans),
    path('inicio/menu/propia',propias),
    path('inicio/menu/clave',claves),
    path('inicio/menu/clave/tercero',cuentaTercero),
    path('inicio/cheques',menuCheques),
    path('inicio/cheques/emitirs',emitirCheque),
    path('inicio/cheques/recibirs',recibirCheque),
    path('inicio/estadocuenta',estados),
    path('inicio/prestamos',prestamos),
    path('administrador/',nose),

]
