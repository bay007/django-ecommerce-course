from django.contrib.auth import login as django_login
from django.contrib.auth import authenticate, get_user_model, logout
from django.shortcuts import redirect, render
from django.utils.http import is_safe_url

from .forms import Loginform, Registroform

# Create your views here.
User = get_user_model()


def login(request):
    login_form = Loginform(request.POST or None)
    context = {
        "title": "Login",
        "content": "Aqui puede iniciar sesion",
        "form": login_form,
        'base_extend': "base.html"
    }
    next_ = request.GET.get('next_url', None)
    next_post = request.POST.get('next_url', None)
    redirect_path = next_ or next_post
    if request.user.is_authenticated():
        return redirect("/")

    if login_form.is_valid():
        login_data = login_form.cleaned_data
        username = login_data["username"]
        password = login_data["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            django_login(request, user=user)

            if is_safe_url(redirect_path, allowed_hosts=request.get_host()):
                return redirect(redirect_path)
            else:
                return redirect("/")

    return render(request, "login.html", context)


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
    return render(request, "registro.html", context)


def salir(request):
    logout(request)
    return redirect("/")
