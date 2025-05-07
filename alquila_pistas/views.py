from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView

from alquila_pistas.forms import CustomUserCreationForm
from alquila_pistas.models import *


# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/index.html'

class CreateGroupView(CreateView):
    model = Group
    template_name = 'alquila_pistas/create_group.html'
    fields = ['name', 'users', 'court']
    success_url = reverse_lazy("alquila_pistas:create_group")

class AboutView(TemplateView):
    template_name = 'alquila_pistas/about_us.html'

class ContactView(TemplateView):
    template_name = 'alquila_pistas/contact.html'

class RentView(TemplateView):
    template_name = 'alquila_pistas/rent.html'

class JoinGroup(TemplateView):
    template_name = 'alquila_pistas/join_group.html'

class SportsPavilionCourtView(TemplateView):
    template_name = 'alquila_pistas/sports_pavilion_court.html'


class BeachCourtView(TemplateView):
    template_name = 'alquila_pistas/beach_court.html'


def logout_view(request):
    logout(request)
    return redirect("login")


class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


