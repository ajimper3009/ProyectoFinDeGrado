from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm:
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    error_messages = {
        "password_mismatch": ("Las contraseñas no coinciden máquina, ESPABILA"),
    }
    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

