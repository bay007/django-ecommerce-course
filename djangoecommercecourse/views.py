from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import ContactForm


class Home(View):
    title = ""

    def get(self, request):
        return render(request, "base.html", context={"title": self.title, "hello": "Mi tienda en linea"})


class Contact(View):
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


class About(View):
    title = ""

    def get(self, request):
        return render(request, "about.html", context={"title": self.title})
