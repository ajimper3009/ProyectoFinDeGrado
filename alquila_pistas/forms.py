from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

from alquila_pistas.models import *

User = get_user_model()


class CreateGroupForm(forms.ModelForm):
    confirm_reservation = forms.ChoiceField(
        choices=[('True', 'Sí'), ('False', 'No')],
        label='¿Deseas hacer una reserva para este grupo?',
        widget=forms.RadioSelect
    )

    class Meta:
        model = Group
        fields = ['name', 'court']
        labels = {
            'name': 'Nombre del Grupo',
            'court': 'Pista'
        }

class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nombreInput'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'emailInput'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'mensajeTextarea'})
    )


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    error_messages = {
        "password_mismatch": ("Las contraseñas no coinciden, por favor intentelo de nuevo"),
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

