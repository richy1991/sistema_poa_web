"""
Script: init_views.py
Descripción: Este script registra automáticamente las vistas de esta app en el servidor de Django para facilitar el enrutamiento.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Reemplaza estos ejemplos con vistas reales
    path('', views.index, name='index'),  # Vista base de ejemplo
]
