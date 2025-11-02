from django.urls import path
from trabajadores.views import *

urlpatterns = [
    path("", TrabajadorListView.as_view(), name="trabajador_list"),
    path("nuevo/", TrabajadorCreateView.as_view(), name="trabajador_create"),
    path("<str:rut>/", TrabajadorDetailView.as_view(), name="trabajador_detail"),
    path("<str:rut>/editar/", TrabajadorUpdateView.as_view(), name="trabajador_edit"),
    path("<str:rut>/eliminar/", TrabajadorDeleteView.as_view(), name="trabajador_delete"),
]
