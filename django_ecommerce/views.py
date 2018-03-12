from django.contrib.auth import login as django_login, logout
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ContactForm, Loginform, Registroform
User = get_user_model()


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
    if request.user.is_authenticated():
        return redirect("/")

    if registro_form.is_valid():
        registro_data = registro_form.cleaned_data
        username = registro_data['username']
        email = registro_data['email']
        password = registro_data['password']
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect("/login")
    return render(request, "auth/registro.html", context)


def salir(request):
    logout(request)
    return redirect("/")
