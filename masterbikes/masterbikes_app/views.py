from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistroForm
from .models import Usuarios

def login(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        password = request.POST.get('contrasena')
        usuario = Usuarios.objects.filter(email=correo, contrasena=password).first()
        if usuario:
            # Autenticación correcta: redirige o guarda la sesión
            return redirect('alguna_vista')
        else:
            # Muestra un error en el formulario
            return render(request, 'login.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})

def recuperar_contraseña(request):
    return render(request,'recuperar_contrasena.html')

def usuario_creado(request):
    return render(request,'usuario_creado.html')