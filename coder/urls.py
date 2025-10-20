from django.urls import path
from .views import index, crear_cliente, crear_producto, crear_tienda

urlpatterns = [
    path("", index , name="index"),
    path("cliente/nuevo", crear_cliente, name="cliente_form"),
    path("producto/nuevo", crear_producto, name="producto_form"),
    path("tienda/nuevo", crear_tienda, name="tienda_form"),
]