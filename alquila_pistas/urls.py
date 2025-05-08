from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views


app_name = 'alquila_pistas'

urlpatterns = [
    path('', views.IndexView.as_view(), name='IndexView'),
    path('create_group/', views.CreateGroupView.as_view(), name='create_group'),
    path('about_us/', views.AboutView.as_view(), name='AboutView'),
    path('contact/', views.ContactView.as_view(), name='ContactView'),
    path('rent/', views.RentView.as_view(), name='RentView'),
    path('join_group/', views.JoinGroup.as_view(), name='JoinGroup'),
    path('sports_pavilion_court/', views.SportsPavilionCourtView.as_view(), name='SportsPavilionCourtView'),
    path('beach_court/', views.BeachCourtView.as_view(), name='BeachCourtView'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]