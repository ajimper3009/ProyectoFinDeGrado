from datetime import datetime, timedelta
from email.message import EmailMessage
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, FormView, ListView
from alquila_pistas.forms import CustomUserCreationForm, GroupForm
from alquila_pistas.models import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.shortcuts import redirect
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
        group = form.save()

        if form.cleaned_data.get('make_reservation'):
            date = form.cleaned_data.get('date')
            start_time = form.cleaned_data.get('start_time')
            start_datetime = datetime.combine(date, start_time)
            finish_datetime = start_datetime + timedelta(hours=1.5)

            Reservation.objects.create(
                user=self.request.user,
                court=form.cleaned_data.get('court'),
                date=date,
                start_time=start_datetime,
                finish_time=finish_datetime
            )

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

# def simple_mail(request):
#     send_mail(subject='Subject here', message='Here is the message.', from_email='jimenezjotape@gmail.com', recipient_list=['tunnelb76@gmail.com'])
#
#     return HttpResponse('Email sent!')
#
# def message_mail(request):
#     email = EmailMessage(
#         subject='Subject here',
#         body='Here is the message.',
#         from_email='jimenezjotape@gmail.com',
#         to=['tunnelb76@gmail.com'],
#         bcc=['<EMAIL>'],
#         reply_to=['<EMAIL>'],
#     )
#     email.send()
#
#     return HttpResponse('Email sent!')
