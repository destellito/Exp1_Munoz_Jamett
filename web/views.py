from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.views import View
from .models import Producto, Carrito, ItemCarrito
from .forms import ProductoForm
import mercadopago

def index(request):
    return render(request, 'web/index.html')

@login_required
def gallery(request):
    productos = Producto.objects.all()
    return render(request, 'web/gallery.html', {'productos': productos})

def cafe(request):
    return render(request, 'web/cafe.html')

def aboutus(request):
    return render(request, 'web/aboutus.html')

def faq(request):
    return render(request, 'web/faq.html')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request,user)
            return redirect('index')
    return render(request, 'registration/register.html',data)

def product_list(request):
    prod=Producto.objects.all()
    return render(request, 'web/product_list.html',{'prod':prod})

def agregar(request):
    return render(request, 'web/agregar.html')

def agregarrec(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(product_list)
    else:
        form = ProductoForm()
    return render(request, '', {'form': form})

def eliminar(request,id):
    prod=Producto.objects.get(id=id)
    prod.delete()
    return redirect(product_list)

def actualizar(request, id):
    prod=Producto.objects.get(id=id)
    return render(request, 'web/actualizar.html', {'prod':prod})

def actualizarrec(request, id):
    x = request.POST['nombre']
    w = request.POST['descripcion']
    y = request.POST['precio']
    
    prod = Producto.objects.get(id=id)
    prod.nombre = x
    prod.descripcion = w
    prod.precio = y

    if 'imagen' in request.FILES:
        prod.imagen = request.FILES['imagen']

    prod.save()
    return redirect(product_list)

class GalleryView(View):
    template_name = 'web/gallery.html'

    def get(self, request):
        productos = Producto.objects.all()
        return render(request, self.template_name, {'productos': productos})

    def post(self, request):
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))

        if request.user.is_authenticated:
            carrito, created = Carrito.objects.get_or_create(user=request.user)
            producto = Producto.objects.get(id=producto_id)
            item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)

            item.cantidad += cantidad
            item.save()

        return redirect('gallery')

@login_required
def carrito(request):
    try:
        carrito = Carrito.objects.get(user=request.user)
        items = ItemCarrito.objects.filter(carrito=carrito)
        total = sum(item.producto.precio * item.cantidad for item in items)

        return render(request, 'web/carrito.html', {'items': items, 'total': total})
    except Carrito.DoesNotExist:
        items = []
        total = 0

    return render(request, 'web/carrito.html', {'items': items, 'total': total})

@login_required
def eliminar_del_carrito(request, item_id):
    # Eliminar el item del carrito
    try:
        item = ItemCarrito.objects.get(id=item_id)
        item.delete()
    except ItemCarrito.DoesNotExist:
        pass

    return redirect('carrito')

@login_required
def finalizar_compra(request):
    try:
        carrito = Carrito.objects.get(user=request.user)
        items = ItemCarrito.objects.filter(carrito=carrito)
        total = sum(item.producto.precio * item.cantidad for item in items)

        if items.exists():

            sdk = mercadopago.SDK("TEST-6383007846897635-052209-ff5cacd9dcc23954573f14cc46d9b32a-414895471")

            payment_data = {
                "transaction_amount": total,
                "token": "4168818844447115",
                "description": "Payment description",
                "payment_method_id": 'visa',
                "installments": 1,
                "payer": {
                    "email": 'test_user_123456@testuser.com'
                }
            }
            result = sdk.payment().create(payment_data)
            payment = result["response"]

            print(payment)

            carrito.productos.clear()

            return render(request, 'web/finalizar_compra.html')
    except Carrito.DoesNotExist:
        pass

    return redirect('carrito')