from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "border-solid border border-black rounded w-full mb-5 p-2"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "border-solid border border-black rounded w-full mb-5 p-2"
    }))


class RegisterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"class": "border-solid border border-black rounded w-full mb-5 p-2"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={"class": "border-solid border border-black rounded w-full mb-5 p-2"}))
    password2 = forms.CharField(label="Confirmación password", widget=forms.PasswordInput(
        attrs={"class": "border-solid border border-black rounded w-full mb-5 p-2"}))

    def clean(self):
        super().clean()
        if self.cleaned_data.get("password") != self.cleaned_data.get("password2"):
            self.add_error('password', "Error: Passwords mistmatch")
            self.add_error('password2', "Error: Passwords mistmatch")
