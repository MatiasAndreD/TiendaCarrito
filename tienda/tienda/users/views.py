from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, ListView, CreateView,DeleteView
from tienda.Trabajos.models import Trabajo
from tienda.Productos.models import Producto,Comentario,CarritoCompras
from django.db.models import Q, Max, Min
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


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
    
class DetalleProducto(DetailView):
    template_name = 'detalle.html'
    model = Producto
    

class ComentarioProducto(CreateView):
    template_name = 'detalle.html'
    model = Comentario
    fields = ('comentario','usuario', 'producto',)

    def get_success_url(self):
        return "/detalle_producto/{}/".format(self.object.producto.pk)


class Salir(LogoutView):
	next_page = reverse_lazy('inicio')

class Ingresar(LoginView):
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			return HttpResponseRedirect(reverse('inicio'))
		else:
			context = self.get_context_data(**kwargs)
			return self.render_to_response(context)

	def get_success_url(self):
		return reverse('inicio')

class CambiarPerfil(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('telefono','last_name','first_name','email',)
    success_url ='cambiar_perfil'
    template_name = 'perfil.html'

    def get_object(self,queryset=None):
        return self.request.user


class addACarrito(LoginRequiredMixin, CreateView):
    model = CarritoCompras
    fields = ('usuario','producto','precio')
    success_url = reverse_lazy('inicio')
    login_url = 'ingresar'

class EliminarCarrito(LoginRequiredMixin,DeleteView):
    queryset = CarritoCompras.objects.filter(comprado=False)
    model = CarritoCompras
    success_url = reverse_lazy('inicio')
    login_url = 'ingresar'

class ListarCarrito(LoginRequiredMixin,ListView):
    template_name = 'carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarrito, self).get_context_data(**kwargs)
        context['tab'] = 'sincomprar'
        return context

class ListarCarritoPendientes(LoginRequiredMixin,ListView):
    template_name = 'carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=False,pendiente=True)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoPendientes, self).get_context_data(**kwargs)
        context['tab'] = 'pendientes'
        return context

class ListarCarritoFinalizadas(LoginRequiredMixin,ListView):
    template_name = 'carrito.html'
    model = CarritoCompras
    queryset = CarritoCompras.objects.filter(comprado=True,pendiente=False)
    login_url = 'ingresar'

    def get_context_data(self, **kwargs):
        context = super(ListarCarritoFinalizadas, self).get_context_data(**kwargs)
        context['tab'] = 'finalizadas'
        return context