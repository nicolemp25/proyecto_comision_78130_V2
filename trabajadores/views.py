from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.db.models import Q

from trabajadores.forms import TrabajadorForm
from trabajadores.models import Trabajador


class TrabajadorListView(ListView):
    model = Trabajador
    template_name = 'trabajadores/trabajador_list.html'
    context_object_name = 'trabajadores'
    paginate_by = 20  # opcional

    def get_queryset(self):
        q = self.request.GET.get('q', '').strip()
        qs = Trabajador.objects.all().order_by('-fecha_creacion')
        if q:
            qs = qs.filter(
                Q(nombre__icontains=q) |
                Q(apellido__icontains=q) |
                Q(tienda__icontains=q) |
                Q(rut__icontains=q)
            )
        return qs


class TrabajadorCreateView(CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajadores/trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')


class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajadores/trabajador_form.html'
    success_url = reverse_lazy('trabajador_list')
    # usar RUT como slug:
    slug_field = 'rut'
    slug_url_kwarg = 'rut'


class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = 'trabajadores/trabajador_confirm_delete.html'
    success_url = reverse_lazy('trabajador_list')
    slug_field = 'rut'
    slug_url_kwarg = 'rut'


class TrabajadorDetailView(DetailView):
    model = Trabajador
    template_name = 'trabajadores/trabajador_detail.html'
    slug_field = 'rut'
    slug_url_kwarg = 'rut'
