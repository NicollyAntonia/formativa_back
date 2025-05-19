from django.urls import path
from .views import (RegistroUsuarioView, LoginUsuarioView,ProfessorCreateView, ProfessorListView, ProfessorUpdateView, ProfessorDeleteView,DisciplinaCRUDView, ReservaAmbienteCRUDView,MinhasDisciplinasView, MinhasReservasView)

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('professores/', ProfessorListView.as_view()),
    path('professores/criar/', ProfessorCreateView.as_view()),
    path('professores/<int:pk>/editar/', ProfessorUpdateView.as_view()),
    path('professores/<int:pk>/deletar/', ProfessorDeleteView.as_view()),
    path('disciplina/', DisciplinaCRUDView.as_view()),
    path('reservar/', ReservaAmbienteCRUDView.as_view()),
    path('disciplinas/', MinhasDisciplinasView.as_view()),
    path('reservas/', MinhasReservasView.as_view()),
]
