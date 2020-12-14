from django.urls import path
from PROYECTO.views import saludar,administrador,seleccionarCliente,crearPersona,crearEmpresa,clientes,inicios,ahorro,ventanaproveedorbasico,proveedor,proveedores
from PROYECTO.views import trans,propias,cuentaTercero,menuCheques,emitirCheque,recibirCheque,estados,prestamos
urlpatterns = [
    path('',saludar),
    path('administrador/',administrador),
    path('administrador/crear/',seleccionarCliente),
    path('administrador/crear/persona/',crearPersona),
    path('administrador/crear/empresa/',crearEmpresa),
    path('cliente/',clientes),
    path('cliente/inicio',inicios),
    path('cliente/inicio/crear_ahorro',ahorro),
    path('cliente/inicio/pagos',ventanaproveedorbasico),
    path('cliente/inicio/pagos/proveedorEmpleado',proveedor),
    path('cliente/inicio/pagos/basico',proveedores),
    path('cliente/inicio/menu',trans),
    path('cliente/inicio/menu/propia',propias),
    path('cliente/inicio/menu/tercero',cuentaTercero),
    path('cliente/inicio/cheques',menuCheques),
    path('cliente/inicio/cheques/emitirs',emitirCheque),
    path('cliente/inicio/cheques/recibirs',recibirCheque),
    path('cliente/inicio/estadocuenta',estados),
    path('cliente/inicio/prestamos',prestamos),

]
