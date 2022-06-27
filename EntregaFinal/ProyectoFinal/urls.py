"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from App.urls import *
from Applogin.urls import *
from AppRegistro.views import *
from Applogin.views import *
from App.views import *

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", include("App.urls")),
    path('', include("App.urls")),
    path("accounts/profile", perfil_usuario, name="Perfil"),
    path("accounts/logout", LogoutView.as_view(template_name="Applogin/gracias_logout.html"), name = "Logout"),
    path("accounts/login", login_request, name="Login"),
    path("accounts/register", register, name="Register"),
    path("", include("Applogin.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 