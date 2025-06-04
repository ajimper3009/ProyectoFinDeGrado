from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import UserProfileView, CourtDetailView

app_name = 'alquila_pistas'

urlpatterns = [

    #Ruta para la vista Principal
    path('', views.IndexView.as_view(), name='IndexView'),
    #Ruta para Crear un Grupo
    path('create-group/', views.CreateGroupView.as_view(), name='create_group'),
    #Ruta para la vista de Sobre Nosotros
    path('about-us/', views.AboutView.as_view(), name='AboutView'),
    #Ruta para la vista de Perfil
    path('profile/', UserProfileView.as_view(), name='profile'),
    #Ruta para actualizar la foto del Perfil
    path('update-profile-image/', views.UpdateProfileImageView.as_view(), name='update_profile_image'),
    #Ruta para la vista de Contacto
    path('contact/', views.ContactView.as_view(), name='ContactView'),
    #Ruta para la vista deUnirse a un Grupo
    path('join-group/', views.JoinGroupView.as_view(), name='JoinGroup'),
    #Ruta para la vista de que te has unido a un grupo correctamente
    path('join-group-success/', views.JoinGroupSuccessView.as_view(), name='JoinGroupSuccessView'),
    #Ruta para la vista de eliminar un grupo
    path('delete-group/', views.DeleteGroupView.as_view(), name='DeleteGroupView'),
    #Ruta para la vista de las pistas de Pabellón
    path('sports-pavilion_court/', views.SportsPavilionCourtView.as_view(), name='SportsPavilionCourtView'),
    #Ruta para la vista de las pistas de Playa
    path('beach-court/', views.BeachCourtView.as_view(), name='BeachCourtView'),
    #Ruta para la vista de detalle de una pista
    path('courts/<int:pk>/', CourtDetailView.as_view(), name='court_detail'),

    #Ruta para el login, logout y registro
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
