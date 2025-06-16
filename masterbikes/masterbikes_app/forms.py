from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repetir contraseña")
    fechaNacimiento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    telefono = forms.CharField(max_length=15)
    rut = forms.CharField(max_length=12)

    def clean_password1(self):
        pwd = self.cleaned_data.get("password1")
        validate_password(pwd)
        return pwd

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password2", "Las contraseñas no coinciden.")
        return cleaned
