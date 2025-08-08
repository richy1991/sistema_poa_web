from django.urls import path
from .views import ObjetivoListCreateView, ObjetivoDetailView

urlpatterns = [
    path('', ObjetivoListCreateView.as_view(), name='objetivo-list-create'),
    path('<int:pk>/', ObjetivoDetailView.as_view(), name='objetivo-detail'),
]
