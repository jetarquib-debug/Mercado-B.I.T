from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from .forms import DatosBasicosForm, UsuarioRegistroForm
from Usuarios.models import Usuario

#crear una funcion para registrar usuarios usando los formularios creados en forms.py
def registrar_usuario(request):
    if request.method == 'POST':
        form_registro = UsuarioRegistroForm(request.POST)
        form_datos = DatosBasicosForm(request.POST)
        
        if form_registro.is_valid() and form_datos.is_valid():
            # Guardar el usuario
            usuario = form_registro.save()
            
            # Guardar los datos básicos
            datos_basicos = form_datos.save(commit=False)
            datos_basicos.id = usuario.id  # Asignar el ID del usuario recién creado
            datos_basicos.save()
            
            messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
            return redirect('login')  # Redirigir a la página de inicio de sesión
        else:
            messages.error(request, 'ERROR. Por favor corrige los errores en el formulario.')
    else:
        form_registro = UsuarioRegistroForm()
        form_datos = DatosBasicosForm()
    
    return render(request, 'registro_usuario.html', {
        'form_registro': form_registro,
        'form_datos': form_datos
    })
        