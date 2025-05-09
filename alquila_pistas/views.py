from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views.generic import TemplateView, CreateView, FormView
from .models import Group, Court, User
from alquila_pistas.forms import CustomUserCreationForm, CreateGroupForm
from alquila_pistas.models import *


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/index.html'


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = CreateGroupForm
    template_name = 'alquila_pistas/create_group.html'
    success_url = reverse_lazy('alquila_pistas:index')

    def form_valid(self, form):
        group = form.save(commit=False)

        if form.cleaned_data['confirm_reservation'] == 'True':
            reservation = Reservation.objects.create(
                user=self.request.user,
                court=group.court,
                date=timezone.now().date(),
                start_time=timezone.now(),
                finish_time=timezone.now() + timezone.timedelta(hours=1.5)
            )
            group.reservation = reservation

        group.save()
        # Añadir el usuario actual al grupo
        group.users.add(self.request.user)
        return super().form_valid(form)


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/about_us.html'

class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/contact.html'

class RentView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/rent.html'

class JoinGroup(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/join_group.html'

    def join_group_view(request):
        # Obtener todos los grupos
        groups = Group.objects.all()

        return render(request, 'alquila_pistas/join_group.html', {'groups': groups})

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
