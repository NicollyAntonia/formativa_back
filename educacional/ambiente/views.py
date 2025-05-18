from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .models import Usuario, Professor, Disciplina, ReservaAmbiente
from .serializers import (
    UsuarioSerializer, ProfessorSerializer,
    DisciplinaSerializer, ReservaAmbienteSerializer
)
from .permissions import IsGestor

# =========================
# 🔐 Registro e Login JWT
# =========================

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            usuario = serializer.save()
            return Response({
                'id': usuario.id,
                'username': usuario.username,
                'telefone': usuario.telefone,
                'is_gestor': usuario.is_gestor
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUsuarioView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'detail': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)


# ===============================
# 👨‍🏫 CRUD de Professores (Gestores)
# ===============================

class ProfessorCreateView(generics.CreateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsGestor]

class ProfessorListView(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsGestor]

class ProfessorUpdateView(generics.UpdateAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsGestor]

class ProfessorDeleteView(generics.DestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsGestor]


# ===============================
# 📘 CRUD de Disciplinas (Gestores)
# ===============================

class DisciplinaCRUDView(generics.ListCreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer
    permission_classes = [IsGestor]


# ===============================
# 🏫 CRUD de Reservas (Gestores)
# ===============================

class ReservaAmbienteCRUDView(generics.ListCreateAPIView):
    queryset = ReservaAmbiente.objects.all()
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsGestor]


# ===============================
# 📚 Visualização para Professores
# ===============================

class MinhasDisciplinasView(generics.ListAPIView):
    serializer_class = DisciplinaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Disciplina.objects.filter(professor_responsavel__usuario=self.request.user)

class MinhasReservasView(generics.ListAPIView):
    serializer_class = ReservaAmbienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ReservaAmbiente.objects.filter(professor__usuario=self.request.user)
