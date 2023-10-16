from django.shortcuts import render
from rest_framework import viewsets


from .models import Usuario
from .serializers import UsuarioSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from dj_rest_auth.views import LoginView
from .serializers import LoginSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    #permission_classes = (IsAuthenticated,)
"""""
class CustomLoginView(LoginView):
    serializer_class= LoginSerializer
    permission_classes = (AllowAny)
"""""