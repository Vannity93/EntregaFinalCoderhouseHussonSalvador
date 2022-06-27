from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *
import random
from Applogin.views import *
from django.contrib.auth.models import User
from django.template import Context
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
    return render (request, "App/inicioConBlogs.html",)

#fomulario para crear blog
@login_required
def crear_blog(request):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    if request.method == "POST":

        miFormulario = CrearBlogFormulario(request.POST, request.FILES)
        print(miFormulario)
        
        
        user = request.user.username
        if miFormulario.is_valid():
           informacion = miFormulario.cleaned_data
           blog = Blog(titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], creador=user, contenido=informacion['contenido'], foto=informacion['foto'])
           blog.save()
           return render (request, "App/gracias_blog.html")

    else:

        miFormulario = CrearBlogFormulario()
    
    return render (request, "App/crear_blog.html", {"miFormulario": miFormulario ,"fotoAvatar": avatares[0].imagen.url})

#Vista para generar un blog random en el incio del blog
def random_blog(request):

    avatares = Avatar.objects.filter(user_id=request.user.username)
    rblog = list(Blog.objects.all())
    
    
    if request.user.is_authenticated:
        
        if len(rblog) > 4:
            
            rblog = random.sample(rblog,5)
            return render (request, "App/inicio_con_blogs.html", {"rblog": rblog[0], "rcreador":rblog[1], "rcontenido":rblog[2], "rcreacion":rblog[3], "rfoto":rblog[4].foto.url, "fotoAvatar": avatares[0].imagen.url})
        
        else:
            return render(request, "App/inicio_sin_blogs.html", {"fotoAvatar": avatares[0].imagen.url})
    
    else:
        if len(rblog) > 4:
            
            rblog = random.sample(rblog,5)
            return render (request, "App/inicio_con_blogs.html", {"rblog": rblog[0], "rcreador":rblog[1], "rcontenido":rblog[2],"rfoto":rblog[4],  "rcreacion":rblog[3], "rfoto":rblog[0].foto.url})
            
        else:

            return render(request, "App/inicio_sin_blogs.html")

#vista para mensajes entre usuarios
def mensaje(request):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    mensajes = Mensajes.objects.all()
    mensajes = Mensajes.objects.filter(destinatario_id=request.user.username)
    

    if request.method == "POST":
            
            miFormulario = MensajesFormulario(request.POST)
            print(miFormulario)
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                mensaje = Mensajes (remitente=request.user, destinatario_id = informacion["destinatario"],contenido = informacion["contenido"])
                try:
                    mensaje.save()
                    return render(request, "App/mensaje.html", {"mensajes":mensajes,"fotoAvatar": avatares[0].imagen.url})
                except:
                    mensaje = "EROR! El usuario al que desea enviar el mensaje no existe"
                    return render(request, "App/mensaje.html", {"mensajes":mensajes,"mensaje":mensaje, "fotoAvatar": avatares[0].imagen.url})


        
    else:
            miFormulario = MensajesFormulario()
            return render (request, "App/mensaje.html", {"miFormulario":miFormulario, "mensajes":mensajes,"fotoAvatar": avatares[0].imagen.url})

    return  render(request, "App/mensaje.html", {"mensajes":mensajes,"fotoAvatar": avatares[0].imagen.url})

#vistas para listar todos los blogs    
def leer_blogs(request):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    blogs = Blog.objects.all()
    
    if request.user.is_authenticated:

        if len(blogs) == 0:
            mensaje = "No hay blogs, disculpe las molestias. Para crear el primero ingrese al sigueinte link."
            return render(request, "App/no_blogs.html", {"mensaje": mensaje, "fotoAvatar": avatares[0].imagen.url})
        else:
            contexto = {"blogs":blogs, "fotoAvatar": avatares[0].imagen.url}

            return render (request, "App/blogs.html", contexto)    
    
    else:

        if len(blogs) == 0:
            mensaje = "No hay blogs, disculpe las molestias. Inicia sesion o crea una cuenta para poder escribir tu blog!"
            return render(request, "App/no_blogs.html", {"mensaje": mensaje})
        else:  
            contexto = {"blogs":blogs, "url2": blogs[0].foto.url}

            return render (request, "App/blogs.html", contexto) 

#Vista para eliminar un blog
@login_required
def eliminar_blogs( request, pk):
    
    try:
        blogs = Blog.objects.get(id=pk)
        blogs.delete()

        return redirect ("/")
    except Exception as exc:
        return redirect ("/")

#Vista para modificar un blog
@login_required
def modificar_blogs(request, pk):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    blogs = Blog.objects.get(id=pk)

    if request.method == "POST":
        miFormulario = CrearBlogFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            blogs.titulo = informacion["titulo"]
            blogs.subtitulo = informacion["subtitulo"]
            blogs.contenido = informacion["contenido"]
            blogs.foto = informacion["foto"]
        
            blogs.save()

            return redirect ("/")
    else:

        miFormulario = CrearBlogFormulario(initial={"titulo":blogs.titulo,"subtitulo":blogs.subtitulo, "contenido":blogs.contenido, "fotoAvatar": avatares[0].imagen.url})

    return render (request, "App/editar_blog.html", {"miFormulario":miFormulario, "pk":pk, "fotoAvatar": avatares[0].imagen.url})

#Vista para leer un blog en especifico
def blog_especifico(request, pk):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    blogEspecifico = Blog.objects.get(id=pk)
    
    if request.user.is_authenticated:
        contexto = {"blogEspecifico":blogEspecifico , "fotoAvatar": avatares[0].imagen.url, "url2": blogEspecifico.foto.url}
        return render (request, "App/blog_especifico.html", contexto)
    
    else:
        contexto = {"blogEspecifico":blogEspecifico}
        return render (request, "App/blog_especifico.html", contexto)

#vista para los avatars
def foto(request):
    
    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    return render(request, "App/padre.html", {"url":avatares[0].imagen.url} )

#vista para editar el perfil de usuario
def editar_perfil(request):

    usuario = request.user
    avatares = Avatar.objects.filter(user_id=request.user.username)

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)
        
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            usuario.email = informacion["email"]
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.password1 = informacion["password1"]
            usuario.passwprd2 = informacion["password2"]
            usuario.save()

            return redirect ("/")
    
    else:
        miFormulario = UserEditForm(initial={"email":usuario.email,"first_name":usuario.first_name, "last_name":usuario.last_name})
        

    return render(request, "App/editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario, "fotoAvatar":avatares[0].imagen.url})

#vista para visualizar los datos del usuario
def perfil_usuario(request):


    avatares = Avatar.objects.filter(user_id=request.user.username)
    usuario = User.objects.get(username=request.user.username)
    redes = RedesSociales.objects.filter(user=request.user.username)

    contexto = {"usuario":usuario, "fotoAvatar": avatares[0].imagen.url, "redes":redes}

    return render (request, "App/perfil_usuario.html", contexto)

#Vista para el sobre mi de la pagina
def about(request):
    avatares = Avatar.objects.filter(user_id=request.user.username)
    
    if request.user.is_authenticated:
        return render (request, "App/about.html", {"fotoAvatar":avatares[0].imagen.url})
    else:
        return render (request, "App/about.html")


