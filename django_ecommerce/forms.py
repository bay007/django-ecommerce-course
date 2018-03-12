from django import forms


class ContactForm(forms.Form):
    attrs = {
        "class": "form-control",
    }
    fullname = forms.CharField(widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(widget=forms.TextInput(attrs=attrs))
    content = forms.CharField(widget=forms.Textarea(attrs=attrs))
