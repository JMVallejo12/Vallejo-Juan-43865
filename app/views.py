
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

# Create your views here.

#Funcion del index
def index(request):

    return render(request, "app/index.html")


#___________________________________________________
#Class based view de los Hoteles
class HotelesList(LoginRequiredMixin, ListView): 
    model = Hotel


class HotelCreate(CreateView):
    model = Hotel
    fields = ['nombre','estrellas','ubicacion']
    success_url = reverse_lazy('hoteles')

class HotelUpdate(LoginRequiredMixin, UpdateView):
    model = Hotel
    fields = ['nombre','estrellas','ubicacion']
    success_url = reverse_lazy('hoteles')

class HotelDelete(LoginRequiredMixin, DeleteView):
    model = Hotel
    success_url = reverse_lazy('hoteles')

#Reserva de hotel
class ReservaCreate(LoginRequiredMixin, CreateView):
    model = Reserva
    fields = ['nombre','apellido','fecha','hotel']
    success_url = reverse_lazy('hoteles')



#__________________________________________________________
#Class based view de los restaurantes
class RestauranteList(LoginRequiredMixin, ListView):
    model = Restaurante

class RestauranteUpdate(LoginRequiredMixin, UpdateView):
    model = Restaurante
    fields = ['nombre', 'ubicacion', 'calificacion']
    success_url = reverse_lazy('restaurantes')

class RestauranteDelete(LoginRequiredMixin, DeleteView):
    model = Restaurante
    success_url = reverse_lazy('restaurantes')

class RestauranteCreate(LoginRequiredMixin, CreateView):
    model = Restaurante
    fields = ['nombre', 'ubicacion', 'calificacion']
    success_url = reverse_lazy('restaurantes')


#___________________________________________________________________
#Class based view de las ciuidades
class CiudadList(LoginRequiredMixin, ListView):
    model = Ciudad

class CiudadUpdate(LoginRequiredMixin, UpdateView):
    model = Ciudad
    fields = ['nombre', 'habitantes', 'superficie']
    success_url = reverse_lazy('ciudades')

class CiudadCreate(LoginRequiredMixin, CreateView):
    model = Ciudad
    fields = ['nombre', 'habitantes', 'superficie']
    success_url = reverse_lazy('ciudades')

class CiudadDelete(LoginRequiredMixin, DeleteView):
    model = Ciudad
    success_url = reverse_lazy('ciudades')

#Vista para busan.html
@login_required
def Busan(request):

    return render(request, "app/busan.html")

#Vista para seul.html
@login_required
def Seul(request):

    return render(request, "app/seul.html")

#Vista para daegu.html
@login_required
def Daegu(request):

    return render(request, "app/daegu.html")

#Vista para gyeongju.html
@login_required
def Gyeongju(request):
    
    return render(request, "app/gyeongju.html")


#_______________________________________________________________
#Calss based view de los lugares
class LugarList(LoginRequiredMixin, ListView):
    model = Lugar

class LugarCreate(LoginRequiredMixin, CreateView):
    model = Lugar
    fields = ['nombre', 'ubicacion', 'precioEntrada', 'tipo']
    success_url = reverse_lazy('lugares')

class LugarUpdate(LoginRequiredMixin, UpdateView):
    model = Lugar
    fields = ['nombre', 'ubicacion', 'precioEntrada', 'tipo']
    success_url = reverse_lazy('lugares')

class LugarDelete(LoginRequiredMixin, DeleteView):
    model = Lugar
    success_url = reverse_lazy('lugares')

#Sistema del Login

def login_request(request):
    if request.method == "POST":
        loginForm = AuthenticationForm(request, data=request.POST)
        if loginForm.is_valid():
            usuario = loginForm.cleaned_data.get('username')
            clave = loginForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/perfiles/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, "app/index.html", {"mensaje": f"Bienvenido {usuario}"})

            else:
                return render(request, "app/login.html",{"form":loginForm, "mensaje": "Datos inválidos"})
            
        else:
            return render(request, "app/login.html",{"form":loginForm,"mensaje": "Datos inválidos"})

    loginForm = AuthenticationForm()

    return render(request, "app/login.html", {"form": loginForm})

#Funcion para registrarse

def register(request):
    usuarioForm = RegistroForm()
    if request.method == "POST":
        usuarioForm = RegistroForm(request.POST)
        if usuarioForm.is_valid():
            usuario = usuarioForm.cleaned_data.get('username')
            usuarioForm.save()
            return render(request, "app/index.html")
        
        else:
            pass
            
           

    return render(request, "app/registro.html", {"form": usuarioForm})


#Sistema de edicion de usuario
@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        editarForm = editarUsuarioForm(request.POST)
        
        if editarForm.is_valid():
            
            usuario.username = editarForm.cleaned_data.get('username')
            usuario.email = editarForm.cleaned_data.get('email')
            usuario.password1 = editarForm.cleaned_data.get('password1')
            usuario.password2 = editarForm.cleaned_data.get('password2')
            usuario.last_name = editarForm.cleaned_data.get('last_name')
            usuario.first_name = editarForm.cleaned_data.get('first_name')
            usuario.save()

            return render(request, "app/index.html", {"mensaje": f"Se edito tu usuario correctamente"}) #El mensaje no se lee por un motivo de diseño de la pagina
        
        else:
            return render(request, "app/editarUsuario.html", {"form":editarForm})
        
    
    else:
        editarForm = editarUsuarioForm(instance=usuario)

    return render(request, "app/editarUsuario.html", {"form":editarForm, 'usuario':usuario.username})


#Agregar o cambiar un avatar
def cambiarAvatar(request):
    editarAvatar = avatarForm()
    if request.method == "POST":
        editarAvatar = avatarForm(request.POST, request.FILES) #Se coloca reuqestFiles porque se va a trabajar con archivos binarios
        if editarAvatar.is_valid():
            u = User.objects.get(username=request.user) 

            #Eliminar anterior avatar si es que existe
            avatarAnterior = Avatar.objects.filter(user=u)
            if len(avatarAnterior) > 0: #Comprueba si es que hay un avatar agregado
                avatarAnterior[0].delete() #Si hay se busca en el indice y se borra

            avatar = Avatar(user=u, imagen=editarAvatar.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "app/index.html")

        else:
            editarAvatar = avatarForm()

    return render(request, "app/editarAvatar.html", {"form": editarAvatar})


#Funcion para mostrar acerca de mi
def AcercaDemi(request):

    return render(request, "app/acercademi.html")
