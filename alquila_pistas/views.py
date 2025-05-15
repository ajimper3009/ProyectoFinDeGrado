from email.message import EmailMessage

from django.contrib import messages
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView, DeleteView
from alquila_pistas.forms import CustomUserCreationForm, GroupForm
from alquila_pistas.models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm



# Create your views here.
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/index.html'


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'alquila_pistas/create_group.html'
    success_url = reverse_lazy('alquila_pistas:IndexView')

    def form_valid(self, form):
        group = form.save(commit=False)
        # Convertir el usuario lazy a una instancia real de User
        group.creator = User.objects.get(id=self.request.user.id)
        group.save()

        if form.cleaned_data.get('make_reservation'):

            reservation = Reservation(
                court=form.cleaned_data['court'],
                date=form.cleaned_data['date'],
                start_time=form.cleaned_data['start_time'],
                name=form.cleaned_data['reservation_name'],
                user=User.objects.get(id=self.request.user.id),
                group=group
            )
            reservation.save()

        return super().form_valid(form)


class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/about_us.html'


class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            email_message = EmailMessage(
                'Mensaje de contacto recibido',
                f'Mensaje enviado por {name} <{email}>\n\n{message}',
                email,
                ['d0370296d4-16a4b8@inbox.mailtrap.io'],
                reply_to=[email],
            )

            try:
                email_message.send()
                return redirect(reverse('alquila_pistas:ContactView') + '?ok')
            except:
                return redirect(reverse('alquila_pistas:ContactView') + '?error')

        return self.render_to_response(self.get_context_data(form=form))


class RentView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/rent.html'


class JoinGroupView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'alquila_pistas/join_group.html'
    context_object_name = 'groups'

    def get_queryset(self):
        # Optimizamos la carga de datos relacionados
        return Group.objects.select_related('court', 'reservation').prefetch_related('users').all()



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


class JoinGroupSuccessView(LoginRequiredMixin, TemplateView):
    model = Group
    template_name = 'alquila_pistas/joinGroupSuccess.html'

    def post(self, request, *args, **kwargs):
        # Aquí añadimos la lógica para unir al usuario al grupo
        group_id = request.POST.get('group_id')  # Necesitarás añadir este campo en tu formulario
        try:
            group = Group.objects.get(id=group_id)
            current_user, created = User.objects.get_or_create(
                name=request.user.username,
                defaults={
                    'age': 0,
                    'location': '',
                    'gender_type': 'male'
                }
            )
            group.users.add(current_user)
            return redirect('alquila_pistas:JoinGroupSuccessView')
        except Group.DoesNotExist:
            return redirect('alquila_pistas:JoinGroup')


class DeleteGroupView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/delete_group.html'

    def get(self, request, *args, **kwargs):
        group_id = request.GET.get('group_id')
        try:
            group = Group.objects.get(id=group_id)
            return render(request, self.template_name, {'group': group})
        except Group.DoesNotExist:
            messages.error(request, "El grupo no existe")
            return redirect('alquila_pistas:IndexView')

    def post(self, request, *args, **kwargs):
        group_id = request.POST.get('group_id')
        try:
            group = Group.objects.get(id=group_id)
            if request.user.username in [user.name for user in group.users.all()]:
                group_name = group.name
                group.delete()
                messages.success(request, f'El grupo "{group_name}" ha sido eliminado correctamente')
            else:
                messages.error(request, "No tienes permiso para eliminar este grupo")
        except Group.DoesNotExist:
            messages.error(request, "El grupo no existe")

        return redirect('alquila_pistas:IndexView')



