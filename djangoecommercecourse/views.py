from django.shortcuts import redirect, render
from django.views import View

from .forms import ContactForm


class HomeView(View):
    title = ""

    def get(self, request):
        return render(request, "base.html", context={"title": self.title, "hello": "Mi tienda en linea"})


class ContactView(View):
    title = "Contacto"

    def get(self, request):
        context = {"title": self.title, "contact_form": ContactForm()}
        return render(request, "contact.html", context=context)

    def post(self, request):
        contact_form = ContactForm(request.POST)

        if not contact_form.is_valid():
            context = {"title": self.title, "contact_form": contact_form}
            return render(request, "contact.html", context=context)

        context = {"title": self.title, "contact_form": None}
        return render(request, "contact_successfull.html", context=context)


class AboutView(View):
    title = ""

    def get(self, request):
        return render(request, "about.html", context={"title": self.title})


class WelcomeView(View):
    title = "Welcome"

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("login")
        context = {"title": self.title}
        return render(request, "welcome.html", context=context)
