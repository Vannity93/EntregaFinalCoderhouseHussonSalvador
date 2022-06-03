from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User





class AvatarFormulario(forms.Form):
    imagen = forms.ImageField()

class RedesSocialesFormulario(forms.Form):
    pagina = forms.URLField()

