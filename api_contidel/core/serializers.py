from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer

from .models import Usuario
from .models import Registrar_Certificado_Camara_Comercio
from .models import Registrar_Fornecedor_mercadoria
from .models import Registrar_Localizacao_mercadoria
from .models import Submeter_Factura
from .models import Continente
from .models import Pais
from .models import Provincia
from .models import Municipio
from .models import Categoria
from .models import Produto

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','password','last_login','nome','sobrenome','endereco','telefone','email','nif','especializacao','tipo_veiculo','capacidade_do_armazem','tipo_mercadoria', 'tipo_de_entidade']



class CustomLoginSerializer(LoginSerializer):
    username=None
    
    class Meta:
        model = Usuario
        fields = ['id','nome','email','sobrenome','endereco','telefone','nif','especializacao','tipo_veiculo','capacidade_do_armazem','tipo_mercadoria', 'tipo_de_entidade']



class PasswordResetSerializer(serializers.Serializer):
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()


class Registrar_Certificado_Camara_ComercioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registrar_Certificado_Camara_Comercio
        fields =['id','descricao','certificado', 'id_da_factura']

class Registrar_Fornecedor_mercadoriaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Registrar_Fornecedor_mercadoria
            fields = ['id','nome','email','telefone','continente','pais','provincia','municipio','endereco',]
        

class Registrar_Localizacao_mercadoriaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Registrar_Localizacao_mercadoria
            fields = ['id','nome','email','telefone','continente','pais','provincia','municipio','endereco',]


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Categoria
            fields = ['id','nome']

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
            model = Produto
            fields = ['id', 'id_da_categoria' ,'nome']



class Submeter_FacturaSerializer(serializers.ModelSerializer):
    id_do_fornecedor = serializers.SerializerMethodField()
    id_da_categoria_produto = serializers.SerializerMethodField()
    id_do_produto = serializers.SerializerMethodField()

    class Meta:
            model = Submeter_Factura
            fields = ['id','descricao','total_pago','data_da_compra', 'id_da_categoria_produto', 'id_do_produto', 'id_do_fornecedor','id_da_localizacao','destino_da_mercadoria_pais','destino_da_mercadoria_municipio','destino_da_mercadoria_continente', 'destino_da_mercadoria_provincia', 'peso','dimensao','marca','modelo','ficheiro_da_fatura']

    #mostrar apenas os nomes dos fornecedores em vez do id da chave estrangeira.
    def get_id_do_fornecedor(self, obj):
         return obj.id_do_fornecedor.nome 

    #pela relação ser many to many deve-se fazer um ciclo para percorrer cada elemento da lista e mostrar
    def get_id_da_categoria_produto(self, obj):
         return [categoria.nome for categoria in obj.id_da_categoria_produto.all()] 

    #pela relação ser many to many deve-se fazer um ciclo para percorrer cada elemento da lista e mostrar
    def get_id_do_produto(self, obj):
         return [produto.nome for produto in obj.id_do_produto.all()] 


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
            model = Pais
            fields = ['id', 'id_do_continente', 'nome']


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
            model = Provincia
            fields = ['id', 'id_do_pais', 'nome']


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
            model = Municipio
            fields = ['id', 'id_da_provincia', 'nome']


class ContinenteSerializer(serializers.ModelSerializer):
    class Meta:
            model = Continente
            fields = ['id','nome']

