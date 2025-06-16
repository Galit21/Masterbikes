from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistroForm

def login(request):
    return render(request,'../templates/login.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Aquí guardas usuario, perfil, etc.
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})
