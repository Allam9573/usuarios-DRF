from .models import Usuarios
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
