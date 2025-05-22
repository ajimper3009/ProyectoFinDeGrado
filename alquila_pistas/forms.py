from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from alquila_pistas.models import *

User = get_user_model()


class GroupForm(forms.ModelForm):
    auto_join = forms.BooleanField(
        label='Unirme automáticamente al grupo',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    make_reservation = forms.BooleanField(
        required=False,
        label='¿Quieres hacer una reserva?',
        widget=forms.CheckboxInput(attrs={'class': 'reservation-toggle'})
    )

    reservation_name = forms.CharField(
        max_length=100,
        required=False,
        label='Nombre del usuario que hará la reserva'
    )

    date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha'
    )

    start_time = forms.TimeField(
        required=False,
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label='Hora de inicio'
    )

    class Meta:
        model = Group
        fields = ['name', 'court']
        labels = {
            'name': 'Nombre del grupo',
            'court': 'Pista',
        }

    def clean(self):
        cleaned_data = super().clean()
        make_reservation = cleaned_data.get('make_reservation')

        if make_reservation:
            required_fields = ['court', 'reservation_name', 'date', 'start_time']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'Este campo es requerido si deseas hacer una reserva')

        return cleaned_data


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
        "password_mismatch": "Las contraseñas no coinciden, por favor intentelo de nuevo",
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

