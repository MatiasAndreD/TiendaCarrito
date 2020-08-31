from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, ListView
from tienda.Trabajos.models import Trabajo
from tienda.Productos.models import Producto
from django.db.models import Q, Max, Min


User = get_user_model()

class Indice(TemplateView): 
    template_name = "home.html"

class Nosotros(TemplateView): 
    template_name = "nosotros.html"

class Valores(TemplateView):
    template_name = "valores.html"


class TrabajosR(ListView):
    template_name = "trabajos.html"
    model = Trabajo

    def trabajosrec(self):
        trabajos = Trabajo.object.all()
        return trabajos

class Equipo(TemplateView):
    template_name = "equipo.html"

class Contacto(TemplateView):
    template_name = "contacto.html"

class Tienda(ListView):
    template_name = 'listado_productos.html'
    model = Producto
    paginate_by = 10

    def get_queryset(self):
        query = None

        if ('nombre' in self.request.GET) and self.request.GET['nombre'] != "":
            query = Q(nombre=self.request.GET["nombre"])


        if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
            try:
                if query == None:
                    query = Q(precio__lte=int(float(self.request.GET['maximo'])))
                else:
                    query = query & Q(precio__lte=int(float(self.request.GET['maximo'])))
            except:
                pass


        if ('minimo' in self.request.GET) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(precio__gte=int(float(self.request.GET['minimo'])))
                else:
                    query = query & Q(precio__gte=int(float(self.request.GET['minimo'])))
            except:
                pass


        if query is not None:
            productos = Producto.objects.filter(query)
        else:
            productos = Producto.objects.all()
        return productos
    
    def get_context_data(self, **kwargs):
        context = super(Tienda, self).get_context_data(**kwargs)
        context['maximo'] = Producto.objects.all().aggregate(Max('precio'))['precio__max']
        context['minimo'] = Producto.objects.all().aggregate(Min('precio'))['precio__min']
        return context
    
        
    