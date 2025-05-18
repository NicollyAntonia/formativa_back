from django.urls import path
from .views import (
    RegistroUsuarioView, LoginUsuarioView,
    ProfessorCreateView, ProfessorListView, ProfessorUpdateView, ProfessorDeleteView,
    DisciplinaCRUDView, ReservaAmbienteCRUDView,
    MinhasDisciplinasView, MinhasReservasView
)

urlpatterns = [
    # Autenticação
    path('auth/registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('auth/login/', LoginUsuarioView.as_view(), name='login'),

    # Professores
    path('professores/', ProfessorListView.as_view()),
    path('professores/criar/', ProfessorCreateView.as_view()),
    path('professores/<int:pk>/editar/', ProfessorUpdateView.as_view()),
    path('professores/<int:pk>/deletar/', ProfessorDeleteView.as_view()),

    # Disciplinas
    path('disciplinas/', DisciplinaCRUDView.as_view()),

    # Reservas
    path('reservas/', ReservaAmbienteCRUDView.as_view()),

    # Professores logados
    path('minhas-disciplinas/', MinhasDisciplinasView.as_view()),
    path('minhas-reservas/', MinhasReservasView.as_view()),
]
