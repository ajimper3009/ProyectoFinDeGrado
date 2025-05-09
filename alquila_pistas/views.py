from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, FormView, ListView
from alquila_pistas.forms import CustomUserCreationForm, CreateGroupForm
from alquila_pistas.models import *


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/index.html'


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = CreateGroupForm
    template_name = 'alquila_pistas/create_group.html'
    success_url = reverse_lazy('alquila_pistas:IndexView')

    def form_valid(self, form):
        group = form.save(commit=False)

        # Obtener o crear el usuario basado en el usuario autenticado
        current_user, created = User.objects.get_or_create(
            name=self.request.user.username,
            defaults={
                'age': 0,  # Valor por defecto
                'location': '',  # Valor por defecto
                'gender_type': 'male'  # Valor por defecto
            }
        )

        if form.cleaned_data['confirm_reservation'] == 'True':
            reservation = Reservation.objects.create(
                user=current_user,
                court=group.court,
                date=timezone.now().date(),
                start_time=timezone.now(),
                finish_time=timezone.now() + timezone.timedelta(hours=1.5)
            )
            group.reservation = reservation

        group.save()
        group.users.add(current_user)

        return super().form_valid(form)


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/about_us.html'

class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/contact.html'

class RentView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/rent.html'


class JoinGroupView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'alquila_pistas/join_group.html'
    context_object_name = 'groups'

    def get_queryset(self):
        # Obtener todos los grupos sin exclusión
        groups = Group.objects.all()
        print("Grupos encontrados:", groups)  # Para depuración
        return groups

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print("Contexto:", context['groups'])  # Para depuración
        return context


class SportsPavilionCourtView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/sports_pavilion_court.html'

class BeachCourtView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/beach_court.html'

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
