from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
from django.db.models.functions import datetime

from alquila_pistas.models import *

User = get_user_model()


from django import forms
from .models import Group, Court
from datetime import datetime

class GroupForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Introduce el nombre del grupo',
            'required': True
        })
    )

    make_reservation = forms.BooleanField(
        label='¿Desea hacer una reserva ahora?',
        required=False,
        widget=forms.RadioSelect(choices=[(True, 'Sí'), (False, 'No')])
    )

    court = forms.ModelChoiceField(
        queryset=Court.objects.all(),
        required=False,
        label='Pista',
        widget=forms.Select(attrs={
            'class': 'form-control',
            'placeholder': 'Selecciona una pista'
        })
    )

    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date',
            'min': datetime.now().strftime('%Y-%m-%d')
        })
    )

    time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={
            'class': 'form-control',
            'type': 'time'
        })
    )

    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción del grupo'
        })
    )

    class Meta:
        model = Group
        fields = ['name', 'make_reservation', 'court', 'description']


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

