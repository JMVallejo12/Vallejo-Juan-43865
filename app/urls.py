from django.contrib import admin
from django.urls import include, path
from .views import *

from django.contrib.auth.views import LogoutView

urlpatterns = [
    #Interacciones con el contenido de la pagina
    path('', index, name="index"),
    
    #Rutas y subrutas de hoteles
    path('hoteles/', HotelesList.as_view(), name="hoteles"), #Muestra los hoteles
    path('hoteles/reserva_form/', ReservaCreate.as_view(), name="reserva"), #Hacer reserva
    path('hoteles/actualizar_hotel/<int:pk>/', HotelUpdate.as_view(), name = "hotel_update"),
    path('hoteles/crear_hotel/', HotelCreate.as_view(), name="crear_hotel"),
    path('hoteles/borrar_hotel/<int:pk>', HotelDelete.as_view(), name="borrar_hotel"),
    
    
    #Restaurantes y subrutas
    path('restaurantes/', RestauranteList.as_view(), name="restaurantes"),
    path('restaurantes/restaurante_update/<int:pk>', RestauranteUpdate.as_view(), name="restaurante_update"),
    path('restaurantes/crear_restaurante/', RestauranteCreate.as_view(), name="crear_restaurante"),
    path('restaurantes/borrar_restaurante/<int:pk>/', RestauranteDelete.as_view(), name="borrar_restaurante"),

    #Rutas y subrutas de lugares
    path('lugares/', LugarList.as_view(), name="lugares"),
    path('lugares/crear_lugar', LugarCreate.as_view(), name="crear_lugar"),
    path('lugares/lugar_update/<int:pk>/', LugarUpdate.as_view(), name="lugar_update"),
    path('lugares/borrar_lugar/<int:pk>/', LugarDelete.as_view(), name="borrar_lugar"),

    
    #Rutas y subrutas de ciudades
    path('ciudades/', CiudadList.as_view(), name="ciudades"),
    path('ciudades/ciudad_update/<int:pk>', CiudadUpdate.as_view(), name="ciudad_update"),
    path('ciudades/crear_ciudad/', CiudadCreate.as_view(), name="crear_ciudad"),
    path('ciudades/borrar_ciudad/<int:pk>/', CiudadDelete.as_view(), name="borrar_ciudad"), 
    path('ciudades/busan', Busan, name="busan"),
    path('ciudades/seul', Seul, name="seul"),
    path('ciudades/daegu', Daegu, name="daegu"),
    path('ciudades/gyeonju', Gyeongju, name="gyeongju"),
    
   
    
    #Interacciones que no tienen nada que ver con el contenido de la pagina, si no con su funcionamiento
    path('login/', login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name="app/index.html"), name="logout"),
    path('register/', register, name="registro"),
    path('editarUsuario/', editarUsuario, name="editar_usuario"),
    path('editarAvatar/', cambiarAvatar, name="editar_avatar"),


    #Acerca de mi
    path('acerca_de_mi/', AcercaDemi, name="acerca_de_mi"),
    

    
    
]