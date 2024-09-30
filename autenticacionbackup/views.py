from django.shortcuts import render, redirect

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.


class VRegistro(View):

    def get(self, request):
        form=CustomUserCreationForm()
        return render(request, "registro/registro.html",{"form":form})

    def post(self, request):
        form=CustomUserCreationForm(request.POST)

        if form.is_valid():#si el formulario es valido, hacer lo que sigue
            usuario=form.save()

            login(request, usuario)

            return redirect('Home') #redireccionamos hacia el home, para cuando ya estemos logueados
        
        else:
            for msg in form.error_messages: #es decir, por cada mensaje de error que haya en el formulario
                messages.error(request, form.error_messages[msg])#mostrar el error o errores posibles

            return render(request, "registro/registro.html",{"form":form})# entonces nos devuelve el request, exactamente
                                                                          #a como estaba antes el formulario, pero con los errores mostrados


def cerrar_sesion(request):
    logout(request)

    return redirect('Home') #redireccionamos hacia el home, para cuando ya estemos deslogueados


def logear(request): #nos va a servir para hacer login, iniciar sesion

    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST) # esto se hace para que podamos obtener los datos que ha introducido el usuario
        if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            contra=form.cleaned_data.get("password")
            usuario=authenticate(username=nombre_usuario, password=contra)#esta es la manera de autenticar el usuario
            if usuario is not None:
                login(request, usuario)
                return redirect('Home') #si el usuario existe, me redirige al home
            else:       #por si el usuario no existe entra al else
                messages.error(request, "usuario no valido")
        else:   #en caso de que la informacion del usuario no se haya introducido correctamente
            messages.error(request, "informacion incorrecta")



    form=AuthenticationForm()
    return render(request, "login/login.html",{"form":form})