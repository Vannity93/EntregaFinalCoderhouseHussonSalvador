from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, to_field="username", on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatars")

    def __str__(self):
        return f"{self.user}"

class RedesSociales(models.Model):
    user = models.OneToOneField(User, to_field="username", on_delete=models.CASCADE)
    pagina = models.URLField(blank=True, null=True)


    def __str__(self):
            return f"{self.user}"


    


