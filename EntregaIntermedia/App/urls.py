from django.urls import path
from App import views


urlpatterns = [
    
    path("", views.random_blog, name = "Inicio"),
    path("inicio", views.random_blog, name = "Inicio"),
    path("create_blog", views.crear_blog, name="CrearBlog"),
    path("messages", views.mensaje, name = "Mensajes"),
    path("pages", views.leer_blogs, name="LeerBlogs"),
    path("eliminar/blog/<pk>", views.eliminar_blogs, name="BorrarBlog"),
    path("edit/blog/<pk>", views.modificar_blogs, name="EditarBlog" ),
    path("pages/<pk>", views.blog_especifico, name="BlogEspecifico" ),
    path("edit/profile", views.editar_perfil, name="EditarPerfil"),
    path("profile", views.perfil_usuario, name="Perfil"),
    path("about", views.about, name="About")
   

]