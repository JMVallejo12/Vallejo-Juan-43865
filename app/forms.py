from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm): #Clase para crear el formulario de registro
    
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields} #Para eliminar los helpers en el formulario

#Editar el usuario
class editarUsuarioForm(UserCreationForm):
    username = forms.CharField(label="Nuevo usuario", max_length=20, required=True)
    email = forms.EmailField(label = "Nuevo correo electronico")
    password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    last_name = forms.CharField(label="Nuevo apellido", max_length=50)
    first_name = forms.CharField(label="Nuevo nombre", max_length=50)
    

    class Meta:
        model = User
        fields = ['email', 'last_name', 'first_name', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

#Formulario para editar el avatar
class avatarForm(forms.Form):
    imagen = forms.ImageField(required=True)



    