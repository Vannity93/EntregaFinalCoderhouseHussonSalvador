from django.urls import path
from Applogin import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [

    
    path("Avatar", views.agregar_avatar, name="AgregarAvatar" ),
    path("delete/avatar", views.borrar_avatar, name="BorrarAvatar"),
    path("redes", views.agregar_redes, name="RedesSociales"),
    path("create/redes", views.crear_redes, name="CrearRedes"),
    path("edit/redes/<pk>", views.modificar_redes, name="EditarRedes" ),
    path("del/redes/<pk>", views.eliminar_redes, name="EliminarRedes"),
    path("change_password", views.cambiar_contrasenia, name="ResetPass")
]