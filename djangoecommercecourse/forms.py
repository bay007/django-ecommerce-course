from django import forms

FULL_INPUT_WIDGET = forms.TextInput(attrs={"class": "w-full mb-5 border-solid border border-black rounded"})


class ContactForm(forms.Form):
    fullname = forms.CharField(label="Nombre completo", widget=FULL_INPUT_WIDGET)
    email = forms.EmailField(label="Email", widget=FULL_INPUT_WIDGET)
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(
        attrs={"class": "w-full mb-5 border-solid border border-black rounded"}))

    def clean_email(self):
        super().clean()
        allowed_emails = set(["gmail.com"])
        print(allowed_emails.intersection(set(self.cleaned_data.get("email").split("@")[1])))
        if len(allowed_emails.intersection(set(self.cleaned_data.get("email").split("@")[1]))) == 0:
            raise forms.ValidationError(
                f"Yor email's domain is not allowed, allowed domains: {','.join([_ for _ in allowed_emails])}")
        return self.cleaned_data.get("email")
