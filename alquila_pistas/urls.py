from django.urls import path, include
from . import views


app_name = 'alquila_pistas'

urlpatterns = [
    path('', views.IndexView.as_view(), name='indexView'),
]