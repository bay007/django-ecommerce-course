from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import redirect, render
from django.views import View

from .forms import LoginForm, RegisterForm

User = get_user_model()


class LoginView(View):
    REDIRECT_WELCOME = "welcome"
    title = "Login"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.REDIRECT_WELCOME)
        context = {
            "title": self.title,
            "login_form": LoginForm()
        }
        return render(request, "user_secure/login.html", context=context)

    def post(self, request):
        if request.user.is_authenticated:
            return redirect(self.REDIRECT_WELCOME)
        login_form = LoginForm(request.POST)

        if not login_form.is_valid():
            context = {
                "title": self.title,
                "login_form": login_form
            }
            return render(request, "user_secure/login.html", context=context)
        email = login_form.cleaned_data.get("email")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            context = {
                "user": user
            }
            # Redirect to a success page.
            return render(request, "welcome.html", context=context)
        else:
            context = {"title": self.title, "unauthorized": True, "login_form": login_form}
            return render(request, "user_secure/login.html", context=context)
        context = {"authorized": True}
        return render(request, "user_secure/login.html", context={"title": self.title})


class RegisterView(View):
    REDIRECT_WELCOME = "welcome"
    title = "Register"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect(self.REDIRECT_WELCOME)
        context = {
            "register_form": RegisterForm()
        }
        return render(request, "user_secure/register.html", context=context)

    def post(self, request):
        if request.user.is_authenticated or User.objects.filter(email=request.POST.get("email")).exists():
            return redirect(self.REDIRECT_WELCOME)

        register_form = RegisterForm(request.POST)
        if not register_form.is_valid():
            context = {
                "title": self.title,
                "register_form": register_form
            }
            return render(request, "user_secure/register.html", context=context)
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")

        user = User.objects.create(email=email)
        user.set_password(password)
        user.save()
        context = {
            "title": self.title,
            "user": user
        }
        return render(request, "user_secure/register_ok.html", context=context)
