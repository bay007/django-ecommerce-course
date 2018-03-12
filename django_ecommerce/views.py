from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, Loginform, Registroform
from django.contrib.auth import authenticate, login as django_login


def pagina_casa(request):
    context = {
        "title": "Hola a todos dudues",
        "content": "Bienvenidos"
    }

    if request.user.is_authenticated():
        context.update({"premium_content": "PREMIUM"})
    return render(request, "home.html", context)


def pagina_sobre_nosotros(request):
    context = {
        "title": "Sobre nosotros",
        "content": "Estea es una prueba para ecomerce"
    }
    return render(request, "home.html", context)


def pagina_contacto(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contacto",
        "content": "Contactanos para pdoer ayudarte",
        "form": contact_form
    }

    if contact_form.is_valid():
        # esto yas es un diccionario con la data necesaria
        datos_formulario = contact_form.cleaned_data
        print(datos_formulario)

    return render(request, "contact/view.html", context)


def login(request):
    login_form = Loginform(request.POST or None)
    context = {
        "title": "Login",
        "content": "Aqui puede iniciar sesion",
        "form": login_form
    }

    if request.user.is_authenticated():
        return redirect("/")

    if login_form.is_valid():
        login_data = login_form.cleaned_data
        username = login_data["username"]
        password = login_data["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user=user)
            # Redirect to a success page.
            return redirect("/")

    return render(request, "auth/login.html", context)


def registro(request):
    registro_form = Registroform(request.POST or None)
    context = {
        "form": registro_form,
        "title": "Registro",
        "content": "Aun no se ha registrado? Hagalo",
    }
    if registro_form.is_valid():
        registro_data = registro_form.cleaned_data
    return render(request, "auth/registro.html", context)
