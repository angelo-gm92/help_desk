from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_incidencias, name='lista'),
    path('nueva/', views.crear_incidencia, name='crear'),
]