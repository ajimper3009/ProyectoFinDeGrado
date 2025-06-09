# 🚀 Proyecto Fin de Grado: AlquilaPistas 🏐

### 🏷️ Título del Proyecto
**AlquilaPistas**

### 👨‍💻 Autor del Proyecto
**Alejandro Jiménez Pérez**

---

## 📌 Introducción

AlquilaPistas es una plataforma web destinada a la gestión del alquiler de pistas de voleibol 🏐. Su objetivo principal es facilitar la reserva de instalaciones deportivas, permitiendo a los usuarios gestionar sus alquileres de forma sencilla y eficiente. Además, se busca implementar funcionalidades adicionales como la posibilidad de unirse a grupos ya creados para compartir el uso de una pista y optimizar la organización de eventos deportivos 📅.

---

## 🎯 Objetivos

Los principales objetivos de este proyecto son:

- ✅ Permitir la reserva de pistas de voleibol de manera online.
- ✅ Implementar un sistema de gestión para administradores y usuarios.
- ✅ Facilitar la creación y gestión de grupos de jugadores.
- ✅ Optimizar el uso de las pistas mediante un sistema de horarios y disponibilidad.
- ✅ Ofrecer una experiencia de usuario intuitiva y eficiente.

---

## 🛠️ Tecnologías a Utilizar

Para el desarrollo del proyecto se utilizarán las siguientes tecnologías:

### **🔧 Backend**
- 🐍 **Python** con **Django** para la lógica del servidor y la gestión de la base de datos.
- 🐳 **Docker** para la contenedorización del proyecto y facilitar su despliegue.

### **🎨 Frontend**
- ⚛️ **JavaScript** para la interfaz de usuario interactiva.
- ⚛️ **bootstrap** para el diseño de la página web.

### **🗄️ Base de Datos**
- A determinar según los requerimientos del proyecto (MySQL, PostgreSQL, SQLite, etc.).

---

## 📅 Planificación

Se estima que el desarrollo del proyecto se llevará a cabo en un periodo de **tres meses** ⏳, coincidiendo con la duración de las prácticas. La planificación aproximada es la siguiente:

1️⃣ **Fase de Análisis y Diseño** (Semana 1-2) 📑
   - Definición de requisitos y funcionalidades.
   - Diseño de la arquitectura del sistema.
   
2️⃣ **Fase de Desarrollo** (Semana 3-8) 💻
   - Implementación del backend y configuración de la base de datos.
   - Desarrollo de la interfaz de usuario.
   - Integración de funcionalidades principales.
   
3️⃣ **Fase de Pruebas y Depuración** (Semana 9-10) 🛠️
   - Pruebas unitarias y de integración.
   - Corrección de errores y optimización del rendimiento.
   
4️⃣ **Fase de Despliegue y Documentación** (Semana 11-12) 🚀
   - Preparación del entorno de despliegue.
   - Redacción de la documentación del proyecto.
   - Presentación final 🎤.

---

## 📝 Notas y Comentarios

Las tecnologías marcadas con "?" indican que su uso aún no está completamente definido y podría variar según el desarrollo del proyecto y los requerimientos técnicos 🔍. Cualquier sugerencia o recomendación será bienvenida para mejorar la planificación y ejecución del proyecto.

---

📌 **Este documento podrá actualizarse conforme se avance en el desarrollo y se definan mejor los detalles técnicos y funcionales del proyecto.** 🚀

---

# 🏐 AlquilaPistas – Plataforma de Alquiler de Pistas de Voleibol

> **Proyecto Fin de Grado** – Alejandro Jiménez Pérez  
> [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
> ![Django](https://img.shields.io/badge/Django-5.2.1-green)
> ![Python](https://img.shields.io/badge/Python-3.11+-blue)

## 📋 Descripción
**AlquilaPistas** es una plataforma web desarrollada con Django cuyo objetivo es facilitar la reserva de pistas de voleibol. Permite a los usuarios consultar disponibilidad, realizar reservas y gestionar sus alquileres de forma sencilla y eficiente.

---

## 🚀 Funcionalidades principales
- 🔐 **Autenticación de usuarios**: Registro, login y logout.
- 📆 **Calendario interactivo**: Visualización y reserva de pistas.
- 🏐 **Gestión de pistas**: Filtrado por ubicación (geopy) y disponibilidad.
- 🛠️ **Panel de administración**: Gestión avanzada para administradores.
- 🖼️ **Soporte multimedia**: Subida de imágenes (Pillow).
- 🐘 **Base de datos robusta**: PostgreSQL para escalabilidad.

---

## 🛠️ Tecnologías utilizadas
| Categoría       | Tecnologías                                                                 |
|-----------------|----------------------------------------------------------------------------|
| Backend         | ![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python) ![Django](https://img.shields.io/badge/Django-5.2.1-092E20?logo=django) |
| Base de datos   | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql) ![Psycopg2](https://img.shields.io/badge/psycopg2-binary-4169E1) |
| Geocalización   | ![GeoPy](https://img.shields.io/badge/geopy-2.3.0-lightgrey)               |
| Frontend        | HTML5, CSS3, Bootstrap                                                     |
| DevOps          | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker) ![Docker Compose](https://img.shields.io/badge/Docker_Compose-2496ED) |

---

## 🧱 Estructura del proyecto
```plaintext
ProyectoFinDeGrado/
│
├── AlquilaPistas/          # Configuración global de Django
├── alquila_pistas/         # App principal
│   ├── templates/          # Vistas HTML
│   ├── static/             # CSS, JS, imágenes
│   └── models.py           # Modelos de base de datos
│
├── manage.py
├── requirements.txt
├── docker-compose.yml      # Configuración Docker
└── Dockerfile
```
## ⚙️ Instalación
### 1. Método local
```
Clona el repositorio:

git clone https://github.com/tu-usuario/alquilapistas.git
cd alquilapistas
Configura el entorno virtual:

python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
Configura las variables de entorno:

cp .env.example .env
Edita el archivo .env con tus credenciales.

Migraciones e inicio:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 2. 🐳 Método con Docker
```
docker compose build
docker compose up -d
```


## 📄 Licencia
```
Distribuido bajo la licencia MIT. Consulta el archivo LICENSE para más información.
```


## 👤 Contacto
```
Alejandro Jiménez Pérez
📧 jimenezjotape@gmail.com
🔗 GitHub
```

---
# 🚀 Vistas

## IndexView

```python
"""
    Vista principal donde estará todo el contenido principal de la página.
    Muestra la página de inicio con contenido accesible solo para usuarios autenticados.
"""
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/index.html'
```
---
## CreateGroupView
```python

"""
    Vista para crear un grupo.
    Permite a un usuario autenticado crear un grupo y asignarse como creador.
    Opcionalmente, permite hacer una reserva asociada al grupo si el formulario lo indica.
"""
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
                finish_time=form.cleaned_data['finish_time'],
                name_reservation=form.cleaned_data['reservation_name'],
                user=User.objects.get(id=self.request.user.id),
                group=group
            )
            reservation.save()

        return super().form_valid(form)
```
---
## AboutView
```python
"""
    Vista que muestra información 'Sobre nosotros'.
    Presenta detalles sobre la empresa o proyecto en una página estática.
"""
class AboutView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/about_us.html'
```
---
## ContactView
```python
"""
    Vista para enviar mensajes de contacto.
    Permite a usuarios autenticados enviar un formulario de contacto.
    Envía un email al administrador y muestra mensajes de éxito o error.
"""
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

```
---
## JoinGroupView
```python
"""
    Vista para unirse a grupos existentes.
    Muestra una lista de todos los grupos disponibles con sus datos relacionados.
    Facilita al usuario elegir y unirse a un grupo.
"""
class JoinGroupView(LoginRequiredMixin, ListView):
    model = Group
    template_name = 'alquila_pistas/join_group.html'
    context_object_name = 'groups'

    def get_queryset(self):
        # Optimizamos la carga de datos relacionados
        return Group.objects.select_related('court', 'reservation').prefetch_related('users').all()

```
---
## SportsPavilionCourtView
```python
"""
    Vista informativa para las pistas del pabellón deportivo.
    Muestra detalles o imágenes de estas pistas para el usuario.
"""
class SportsPavilionCourtView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/sports_pavilion_court.html'

```
---
## BeachCourtView
```python
"""
    Vista informativa para las pistas de playa.
    Muestra detalles o imágenes de estas pistas para el usuario.
"""
class BeachCourtView(LoginRequiredMixin, TemplateView):
    template_name = 'alquila_pistas/beach_court.html'

```
---
## RegisterView
```python
"""
    Vista para registrar nuevos usuarios.
    Muestra el formulario de registro y, tras crear el usuario, inicia sesión automáticamente.
"""
class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
        
```
---
## JoinGroupSuccessView
```python
"""
    Vista que confirma que un usuario se ha unido con éxito a un grupo.
    Añade al usuario a la lista de miembros del grupo seleccionado y muestra mensaje de éxito o error.
"""


class JoinGroupSuccessView(LoginRequiredMixin, TemplateView):
    model = Group
    template_name = 'alquila_pistas/joinGroupSuccess.html'

    def post(self, request, *args, **kwargs):
        group_id = request.POST.get('group_id')
        try:
            group = Group.objects.get(id=group_id)

            # Verificar si el usuario ya está en el grupo
            if request.user in group.users.all():
                messages.error(request, "Ya eres miembro de este grupo")
                return redirect('alquila_pistas:JoinGroup')

            # Verificar si el grupo ya tiene 12 personas
            if group.users.count() >= 12:
                messages.error(request, "El grupo ya ha alcanzado el límite máximo de 12 personas")
                return redirect('alquila_pistas:JoinGroup')

            # Si esta bien, añadimos el usuario
            group.users.add(request.user)
            messages.success(request, "Te has unido al grupo exitosamente")
            return redirect('alquila_pistas:JoinGroupSuccessView')

        except Group.DoesNotExist:
            messages.error(request, "El grupo no existe")
            return redirect('alquila_pistas:JoinGroup')
```
---
## DeleteGroupView
```python
"""
    Vista para eliminar grupos.
    Primero muestra una página para confirmar la eliminación.
    Solo permite eliminar el grupo si el usuario pertenece a él.
"""
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
            reservation = Reservation.objects.get(group=group_id)
            group = Group.objects.get(id=group_id)
            if request.user.username in [user.username for user in group.users.all()]:
                group_name = group.name
                group.delete()
                reservation.delete()
                messages.success(request, f'El grupo "{group_name}" ha sido eliminado correctamente')

            else:
                messages.error(request, "No tienes permiso para eliminar este grupo")
        except Group.DoesNotExist:
            messages.error(request, "El grupo no existe")

        return redirect('alquila_pistas:IndexView')
```
---
## UserProfileView
```python
"""
    Vista que muestra el perfil del usuario autenticado.
    Incluye la información personal y las reservas hechas por el usuario.
"""
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

```
---
## UpdateProfileImageView
```python
"""
    Vista para actualizar la imagen de perfil del usuario vía AJAX.
    Recibe una imagen en la petición POST y la guarda, eliminando la anterior si existe.
    Retorna JSON con el resultado (éxito o error).
"""
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
```
---
## CourtDetailView
```python
"""
    Vista que muestra los detalles de una pista específica.
    Permite al usuario ver información detallada de una pista seleccionada.
"""
class CourtDetailView(DetailView):
    model = Court
    template_name = 'alquila_pistas/court_detail.html'
    context_object_name = 'court'
```

