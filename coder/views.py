from django.shortcuts import render, redirect
from coder.forms import *
from coder.models import Tienda
from django.db.models import Q


def index(request):
    return render(request,"coder/index.html")

def crear_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect("index") 
    else:
        form = ClienteForm() 

    return render(request, "coder/cliente_form.html", {'form': form})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = ProductoForm()

    return render(request, "coder/producto_form.html", {"form": form})

def crear_tienda(request):
    if request.method == "POST":
        form = TiendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = TiendaForm()

    return render(request, "coder/tienda_form.html", {"form": form})

def lista_tiendas(request):
    q = request.GET.get('q', '').strip()
    qs = Tienda.objects.all()
    if q:
        qs = qs.filter(
            Q(nombre__icontains=q) |
            Q(zona__icontains=q) |
            Q(direccion__icontains=q) |
            Q(telefono__icontains=q)
        )
    tiendas = qs.order_by('nombre')  # O '-id' si prefieres las más recientes
    return render(request, 'coder/tienda_list.html', {'tiendas': tiendas, 'query': q})
