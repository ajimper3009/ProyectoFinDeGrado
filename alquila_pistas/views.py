from email.message import EmailMessage
from django.contrib import messages
from django.contrib.auth import login
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, FormView, ListView
from alquila_pistas.forms import CustomUserCreationForm, GroupForm
from alquila_pistas.models import *
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ContactForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView



# Create your views here.


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/index.html'


class CreateGroupView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'alquila_pistas/create_group.html'
    success_url = reverse_lazy('alquila_pistas:JoinGroup')

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
                name_reservation=form.cleaned_data['reservation_name'],
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
        group_id = request.POST.get('group_id')
        try:
            group = Group.objects.get(id=group_id)
            # Usamos directamente el usuario actual
            group.users.add(request.user)
            messages.success(request, "Te has unido al grupo exitosamente")
            return redirect('alquila_pistas:JoinGroupSuccessView')
        except Group.DoesNotExist:
            messages.error(request, "El grupo no existe")
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
            if request.user.username in [user.username for user in group.users.all()]:
                group_name = group.name
                group.delete()
                messages.success(request, f'El grupo "{group_name}" ha sido eliminado correctamente')

            else:
                messages.error(request, "No tienes permiso para eliminar este grupo")
        except Group.DoesNotExist:
            messages.error(request, "El grupo no existe")

        return redirect('alquila_pistas:IndexView')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'alquila_pistas/profile.html'
    context_object_name = 'profile_user'

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Manejo seguro de las reservas
        try:
            # Intenta obtener las reservas
            reservations = Reservation.objects.filter(user=self.request.user)
            context['reservations'] = reservations
            context['error_message'] = None
        except Exception as e:
            # Si hay un error, establece una lista vacía y guarda el mensaje de error
            print(f"Error al obtener reservas: {str(e)}")
            context['reservations'] = []
            context['error_message'] = "No se pudieron cargar las reservas en este momento."

        return context


@method_decorator(csrf_exempt, name='dispatch')
class UpdateProfileImageView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({
                'success': False,
                'error': 'Usuario no autenticado'
            }, status=401)

        if not request.FILES.get('profile_image'):
            return JsonResponse({
                'success': False,
                'error': 'No se proporcionó ninguna imagen'
            }, status=400)

        try:
            user_profile = request.user.userprofile
            # Si existe una imagen anterior, la eliminamos
            if user_profile.profile_image:
                user_profile.profile_image.delete(save=False)

            user_profile.profile_image = request.FILES['profile_image']
            user_profile.save()

            return JsonResponse({
                'success': True,
                'message': 'Imagen actualizada correctamente'
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=500)


class CourtDetailView(DetailView):
    model = Court
    template_name = 'alquila_pistas/court_detail.html'
    context_object_name = 'court'









