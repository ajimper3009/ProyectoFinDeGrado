from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
from .views import UserProfileView, CourtDetailView

app_name = 'alquila_pistas'

urlpatterns = [
    path('', views.IndexView.as_view(), name='IndexView'),
    path('create-group/', views.CreateGroupView.as_view(), name='create_group'),
    path('about-us/', views.AboutView.as_view(), name='AboutView'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('update-profile-image/', views.UpdateProfileImageView.as_view(), name='update_profile_image'),
    path('contact/', views.ContactView.as_view(), name='ContactView'),
    path('join-group/', views.JoinGroupView.as_view(), name='JoinGroup'),
    path('join-group-success/', views.JoinGroupSuccessView.as_view(), name='JoinGroupSuccessView'),
    path('delete-group/', views.DeleteGroupView.as_view(), name='DeleteGroupView'),
    path('sports-pavilion_court/', views.SportsPavilionCourtView.as_view(), name='SportsPavilionCourtView'),
    path('beach-court/', views.BeachCourtView.as_view(), name='BeachCourtView'),
    path('courts/<int:pk>/', CourtDetailView.as_view(), name='court_detail'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
