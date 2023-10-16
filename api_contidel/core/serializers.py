from rest_framework import serializers
from .models import Usuario
from dj_rest_auth.serializers import LoginSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','password','last_login','nome','sobrenome','endereco','telefone','email','nif','especializacao','tipo_veiculo','capacidade_do_armazem','tipo_mercadoria', 'tipo_de_entidade']



class CustomLoginSerializer(LoginSerializer):
    class Meta:
        model = Usuario
        fields = ('email','password')
