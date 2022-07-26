from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def super_user_registro(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']

            email = form.cleaned_data['email']

            contrasenia = form.cleaned_data['contrasenia']

            form.save()

            return render(request, "Core/padre.html" , {"mensaje":"Usuario Creado"})

    else:

        form = UserCreationForm()        

    return render(request, "Core/registro.html", {"form": form})

def usuario_registro(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():

            nombre_de_usuario = form.cleaned_data['nombre_de_usuario']

            email = form.cleaned_data['email']

            contrasenia = form.cleaned_data['contrasenia']

            form.save()

            return render(request, "Core/padre.html", {"manesaje":"Usuario Creado"})

    else:

        form = UserCreationForm()

    return render(request,"Core/registro.html", {"form":form})

def super_user_login(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            nombre_de_usuario = form.cleaned_data.get('nombre_de_usuario')

            contrasenia = form.cleaned_data.get('contrasenia')

            user = authenticate(nombre_de_usuario = nombre_de_usuario, contrasenia = contrasenia)

            if user is not None:

                login(request, user)

                return render(request,"Core/padre.html", {"mensaje":f"Bienbenido {nombre_de_usuario}"} )

            else:

                return render(request,"Core/padre.html", {"mensaje":"Error, datos incorrectos"} )

        else:

            return render(request,"Core/padre.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"Core/login.html", {'form':form} )                

def usuario_login(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            nombre_de_usuario = form.cleaned_data.get('nombre_de_usuario')

            contrasenia = form.cleaned_data.get('contrasenia')

            user = authenticate(nombre_de_usuario = nombre_de_usuario , contrasenia = contrasenia)

            if user is not None:

                login(request, user)

                return render(request,"Core/padre.html", {"mensaje":f"Bienvenido {nombre_de_usuario}"} )

            else:

                return render(request,"Core/padre.html", {"mensaje":"Error, datos incorrectos"} )

        else:

            return render(request,"Core/padre.html" , {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"Core/login.html", {'form':form})                    



