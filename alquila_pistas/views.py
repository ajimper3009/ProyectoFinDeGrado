from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.views.generic import TemplateView, CreateView, FormView
from .models import Group, Court, User
from alquila_pistas.forms import CustomUserCreationForm
from alquila_pistas.models import *


# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/index.html'



class CreateGroupView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/create_group.html'
    fields = ['name', 'court', 'users']  # Puedes usar un formulario personalizado también
    success_url = reverse_lazy('home')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.POST = None
        self.method = None

    def crear_grupo(request):
        courts = Court.objects.all()
        users = User.objects.all()

        if request.method == 'POST':
            name = request.POST['name']
            court_id = request.POST['court']
            date = request.POST['date']
            start_time = request.POST['start_time']
            finish_time = request.POST['finish_time']
            selected_user_ids = request.POST.getlist('users')

            start_datetime = timezone.make_aware(parse_datetime(f"{date}T{start_time}"))
            finish_datetime = timezone.make_aware(parse_datetime(f"{date}T{finish_time}"))

            if finish_datetime <= start_datetime:
                messages.error(request, "La hora de fin debe ser posterior a la de inicio.")
                return render(request, 'alquila_pistas/create_group.html', {'courts': courts, 'users': users})

            court = Court.objects.get(id=court_id)

            # Verificar solapamiento de reservas
            conflicto = Reservation.objects.filter(
                court=court,
                date=date,
                start_time__lt=finish_datetime,
                finish_time__gt=start_datetime
            ).exists()

            if conflicto:
                messages.error(request, "La pista ya está reservada en ese horario.")
            else:
                reserva = Reservation.objects.create(
                    user=User.objects.first(),  # Cambia esto según lógica real
                    court=court,
                    date=date,
                    start_time=start_datetime,
                    finish_time=finish_datetime
                )

                grupo = Group.objects.create(name=name, court=court, reservation=reserva)
                grupo.users.set(User.objects.filter(id__in=selected_user_ids))
                messages.success(request, "Grupo creado correctamente.")
                return redirect('nombre_de_tu_home')

        return render(request, 'alquila_pistas/create_group.html', {'courts': courts, 'users': users})

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/about_us.html'

class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/contact.html'

class RentView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/rent.html'

class JoinGroup(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/join_group.html'

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
