from django import forms


class ContactForm(forms.Form):
    attrs = {
        "class": "form-control",
    }
    fullname = forms.CharField(widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs))
    content = forms.CharField(widget=forms.Textarea(attrs=attrs))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if "gmail.com" not in email:
            raise forms.ValidationError("Ingrese un dominio gmail.com")
        return email

    def clean_fullname(self):
        fullname = self.cleaned_data.get("fullname")
        if len(fullname.strip()) < 5 or len(fullname.strip()) > 30:
            raise forms.ValidationError(
                "Su nombre debe tener minimo 5 caracteres y maximo 30")
        return fullname

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content.strip()) < 10 or len(content.strip()) > 50:
            raise forms.ValidationError(
                "Debe tener entre 10 y 50 caracteres ")
        return content


class Loginform(forms.Form):
    attrs = {
        "class": "form-control",
    }
    username = forms.CharField(widget=forms.TextInput(attrs=attrs))
    password = forms.CharField(widget=forms.PasswordInput(attrs=attrs))


class Registroform(forms.Form):
    pass
