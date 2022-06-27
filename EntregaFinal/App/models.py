from django.db import models
import datetime
from django.contrib.auth.models import  User
from ckeditor.fields import RichTextField

# Create your models here.

class Blog(models.Model):

    
    titulo = models.CharField(max_length=40)

    creador = models.CharField(max_length=40,blank=True)
    contenido = RichTextField()
    creacion = models.DateField(auto_now=True)
    foto = models.ImageField(upload_to="avatars", null=True, blank = True)
    subtitulo = models.CharField(max_length=40)
    

    def __str__(self):

        return f"{self.titulo, self.id, self.creador, self.contenido}"
    
class Mensajes(models.Model):
    
    remitente = models.CharField(max_length=40)
    destinatario = models.ForeignKey(User, to_field="username", on_delete=models.CASCADE)
    contenido = models.CharField(max_length=500)
    def __str__(self):

        return f"{self.destinatario}-{self.remitente}-{self.contenido}"
    
