from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'web/index.html')

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
            return redirect('home')
    return render(request, 'registration/register.html',data)