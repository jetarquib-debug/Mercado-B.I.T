from datetime import date
from django import forms
from django.core.exceptions import ValidationError
from Usuarios.models import Usuario

class DatosBasicosForm(forms.ModelForm):
    class Meta:
        # Formulario para los datos básicos del usuario
        model = Usuario
        fields = ['nombres', 'apellidos', 'direccion', 'distrito', 'provincia', 'pais']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'distrito': forms.Select(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
        }
    # clean_nombres y clean_apellidos para validar que solo contengan letras y espacios
    def clean_nombres(self):
        nombres = self.cleaned_data.get("nombres")
        if not nombres.replace(" ", "").isalpha():
            raise ValidationError("Los nombres solo deben contener letras y espacios.")
        return nombres
    
    def clean_apellidos(self):
        apellidos = self.cleaned_data.get("apellidos")
        if not apellidos.replace(" ", "").isalpha():
            raise ValidationError("Los apellidos solo deben contener letras y espacios.")
        return apellidos
    

    # Método para guardar el usuario
    def save(self, commit=True):
        usuario = super().save(commit=False)
        if commit:
            usuario.save()
        return usuario


class UsuarioRegistroForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    contrasena = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirmar Contraseña")
    codigo_pais = forms.ChoiceField(choices=[('1', 'Código de país 1'), ('2', 'Código de país 2')], widget=forms.Select(attrs={'class': 'form-control'}))
    telefono = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dni_ce = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
    # clean_contrasena para validar la contraseña      
    def clean_contrasena(self):
        contrasena = self.cleaned_data.get("contrasena")
        confirmar_contrasena = self.cleaned_data.get("confirmar_contrasena")
        if len(contrasena) < 6:
            raise ValidationError("La contraseña debe tener al menos 6 caracteres.")
        if contrasena != confirmar_contrasena:
            raise ValidationError("Las contraseñas no coinciden.")
        return contrasena
    
    # clean_telefono para validar que el teléfono tenga al menos 7 dígitos y sea positivo
    def clean_telefono(self):
        telefono = self.cleaned_data.get("telefono")
        if not (telefono.isdigit() and len(telefono) >= 7):
            raise ValidationError("El teléfono debe tener al menos 7 dígitos y ser un número positivo.")
        return telefono
    
    # clean_dni_ce para validar que el DNI/CE tenga 8 dígitos y sea positivo
    def clean_dni_ce(self):
        dni_ce = self.cleaned_data.get("dni_ce")
        if dni_ce <= 0 or len(str(dni_ce)) != 8:
            raise ValidationError("El DNI/CE debe tener 8 dígitos y ser un número positivo.")
        return dni_ce
    
    # clean_email para validar que el email no esté ya registrado
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Usuario.objects.filter(email=email).exists():
            raise ValidationError("El correo electrónico ya está registrado.")
        return email
    
    # Método para guardar el usuario
    def save(self):
        datos = self.cleaned_data
        user = Usuario(
            email=datos['email'],
            contrasena=datos['contrasena'],
            telefono=datos['telefono'],
            dni_ce=datos['dni_ce']
        )
        # Aquí deberías encriptar la contraseña antes de guardarla
        user.set_password(user.contrasena)  # Encriptación de la contraseña
        user.save()
        return user
