from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto
from .forms import ProductoForm

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

# def agregarrec(request):
#     x=request.POST['nombre']
#     w=request.POST['descripcion']
#     y=request.POST['precio']
#     z=request.POST['imagen']
#     prod=Producto(nombre=x,precio=y,imagen=z,descripcion=w)
#     prod.save()
#     return redirect(product_list)

def eliminar(request,id):
    prod=Producto.objects.get(id=id)
    prod.delete()
    return redirect(product_list)

def actualizar(request, id):
    prod=Producto.objects.get(id=id)
    return render(request, 'web/actualizar.html', {'prod':prod})

def actualizarrec(request, id):
    x=request.POST['nombre']
    w=request.POST['descripcion']
    y=request.POST['precio']
    z=request.POST['imagen']
    prod=Producto.objects.get(id=id)
    prod.nombre=x
    prod.descripcion=w
    prod.precio=y
    prod.imagen=z
    prod.save()
    return redirect(product_list)