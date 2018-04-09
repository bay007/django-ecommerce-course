from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class Loginform(forms.Form):
    attrs = {
        "class": "form-control",
    }
    username = forms.CharField(widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs))


class Registroform(forms.Form):
    attrs = {
        "class": "form-control",
    }
    username = forms.CharField(
        label="Username", widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(
        label="Email", widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs=attrs))
    password_confirm = forms.CharField(
        label="Confirma Password", widget=forms.PasswordInput(attrs=attrs))

    def clean_username(self):
        username = self.cleaned_data['username']
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Ya existe este usuario")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Ya existe este email")
        return email

    def clean(self):
        data = self.cleaned_data
        if data["password"] != data["password_confirm"]:
            raise forms.ValidationError("Passwords no coinciden")
        return data
