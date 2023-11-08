from django.shortcuts import render
from dj_rest_auth.views import LoginView
from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, AllowAny
from dj_rest_auth.views import LoginView
from .serializers import CustomLoginSerializer

from django.contrib.auth import get_user_model
from dj_rest_auth.views import PasswordResetConfirmView
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from .serializers import PasswordResetSerializer

from .models import Usuario
from .serializers import UsuarioSerializer
from .models import Registrar_Certificado_Camara_Comercio
from .serializers import Registrar_Certificado_Camara_ComercioSerializer
from .models import Registrar_Fornecedor_mercadoria
from .serializers import Registrar_Fornecedor_mercadoriaSerializer
from .models import Registrar_Localizacao_mercadoria
from .serializers import Registrar_Localizacao_mercadoriaSerializer
from .models import Submeter_Factura
from .serializers import Submeter_FacturaSerializer
from .models import Categoria
from .serializers import CategoriaSerializer
from .models import Produto
from .serializers import ProdutoSerializer


from .models import Continente
from .serializers import ContinenteSerializer
from .models import Pais
from .serializers import PaisSerializer
from .models import Provincia
from .serializers import ProvinciaSerializer
from .models import Municipio
from .serializers import MunicipioSerializer



#view do endpoint do continente
class ContinenteViewSet(viewsets.ModelViewSet):
    queryset = Continente.objects.all()
    serializer_class = ContinenteSerializer

    #Aplicação de filtros
    def get_queryset(self):
        queryset = Continente.objects.all()
        nome = self.request.query_params.get('nome')

        if nome:
            queryset = queryset.filter(nome=nome)
            return queryset
        return queryset



#view do endpoint do pais
class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

    #aplicação de filtros
    def get_queryset(self):
        queryset = Pais.objects.all()
        id_do_continente = self.request.query_params.get('id_do_continente')
        nome = self.request.query_params.get('nome')

        if id_do_continente:
            queryset = queryset.filter(id_do_continente=id_do_continente)
            return queryset
        
        if nome:
            queryset = queryset.filter(nome=nome)
            return queryset
        return queryset

#view do endpoint da provincia
class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

    #aplicação de fitros
    def get_queryset(self):
        queryset = Provincia.objects.all()
        id_do_pais = self.request.query_params.get('id_do_pais')
        nome = self.request.query_params.get('nome')

        if id_do_pais:
            queryset = queryset.filter(id_do_pais=id_do_pais)
            return queryset
        
        if nome:
            queryset = queryset.filter(nome=nome)
            return queryset
        return queryset


#view do endpoint do usuário
class MunicipioViewSet(viewsets.ModelViewSet):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

    
    #aplicação de filtros
    def get_queryset(self):
        queryset = Municipio.objects.all()
        id_da_provincia = self.request.query_params.get('id_da_provincia')
        nome = self.request.query_params.get('nome')

        if id_da_provincia:
            queryset = queryset.filter(id_da_provincia=id_da_provincia)
            return queryset
        
        if nome:
            queryset = queryset.filter(nome=nome)
            return queryset
        return queryset













#view do endpoint do usuário
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    

#definição dos campos que serão visiveis após um determinado usuarioS fazer login
class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer
    permission_classes= [AllowAny]

    def get_response(self):
        response = super().get_response()
        if response.status_code == status.HTTP_200_OK:
            user = self.user
            usuario_data = {
                'id': user.id,
                'nome': user.nome,
                'email': user.email,
                'sobrenome': user.sobrenome,
                'endereco': user.endereco,
                'telefone': user.telefone,
                'nif': user.nif,
                'especializacao': user.especializacao,
                'tipo_veiculo': user.tipo_veiculo,
                'capacidade_do_armazem': user.capacidade_do_armazem,
                'tipo_mercadoria': user.tipo_mercadoria,
                'tipo_de_entidade': user.tipo_de_entidade,
                # campos exibidos do usuario que fez login
            }
            response.data['usuario_data'] = usuario_data
        return response




#neste metodo ja não precisa encriptar a palavra passe ao redifir a senha, 
#se não vai dar choque pois a palavra passe ja é encriptada previamente quando o usuário é criado
Usuario = get_user_model()
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    def post(self, request, *args, **kwargs):
        # Verifique se o método HTTP é POST
        if request.method != 'POST':
            return Response({'error': 'Método não permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            nova_senha1 = serializer.validated_data['new_password1']
            nova_senha2 = serializer.validated_data['new_password2']

            # Verifique se as senhas correspondem
            if nova_senha1 == nova_senha2:
                # Continue com o processamento, como você já está fazendo
                uidb64 = kwargs['uidb64']
                token = kwargs['token']
                uid = urlsafe_base64_decode(uidb64).decode()
                try:
                    user = Usuario.objects.get(pk=uid)
                except Usuario.DoesNotExist:
                    return Response({'error': 'Usuário não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

                #user.set_password(nova_senha1) causa conflito de encriptação e não permite fazer login.
                user.password=nova_senha1
                user.save()
                default_token_generator.check_token(user, token)
                return Response({'message': 'Senha redefinida com sucesso!'})
            else:
                return Response({'error': 'As senhas não correspondem.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Registrar_Certificado_Camara_ComercioViewSet(viewsets.ModelViewSet):
    queryset = Registrar_Certificado_Camara_Comercio.objects.all()
    serializer_class = Registrar_Certificado_Camara_ComercioSerializer



class Registrar_Fornecedor_mercadoriaViewSet(viewsets.ModelViewSet):
    queryset = Registrar_Fornecedor_mercadoria.objects.all()
    serializer_class = Registrar_Fornecedor_mercadoriaSerializer


class Registrar_Localizacao_mercadoriaViewSet(viewsets.ModelViewSet):
    queryset = Registrar_Localizacao_mercadoria.objects.all()
    serializer_class = Registrar_Localizacao_mercadoriaSerializer


class Submeter_FacturaViewSet(viewsets.ModelViewSet):
    queryset = Submeter_Factura.objects.all()
    serializer_class = Submeter_FacturaSerializer

    

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    #aplicação de filtros
    def get_queryset(self):
        queryset = Produto.objects.all()
        
        #isto permite que ao passar vários parametros ele retorne uma lista de todos elementos em relação ao parametros que passamos na url.
        id_da_categoria = self.request.query_params.getlist('id_da_categoria')
        nome = self.request.query_params.get('nome')

        if id_da_categoria:
            queryset = queryset.filter(id_da_categoria__in=id_da_categoria)
            return queryset
        
        if nome:
            queryset = queryset.filter(nome=nome)
            return queryset
        return queryset

    

