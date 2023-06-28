from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Producto

def index(request):
    return render(request, 'web/index.html')

@login_required
def gallery(request):
    return render(request, 'web/gallery.html')

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
    x=request.POST['idproducto']
    y=request.POST['nombre']
    z=request.POST['precio']
    w=request.POST['imagen']
    prod=Producto(idproducto=x,nombre=y,precio=z,imagen=w)
    prod.save()
    return redirect("/")

def eliminar(request,id):
    prod=Producto.objects.get(id=id)
    prod.delete()
    return redirect("/")

def actualizar(request, id):
    prod=Producto.objects.get(id=id)
    return render(request, 'actualizar.html', {'prod':prod})

def actualizarrec(request, id):
    x=request.POST['idproducto']
    y=request.POST['nombre']
    z=request.POST['precio']
    w=request.POST['imagen']
    prod=Producto.objects.get(id=id)
    prod.idproducto=x
    prod.nombre=y
    prod.precio=z
    prod.imagen=w
    prod.save()
    return redirect("/")