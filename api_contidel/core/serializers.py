from rest_framework import serializers
from dj_rest_auth.serializers import LoginSerializer
from rest_framework_recursive.fields import RecursiveField


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
from .models import Menu
from .models import TipoUsuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id','password','last_login','nome','sobrenome','endereco','telefone','email','nif','especializacao','tipo_veiculo','capacidade_do_armazem','tipo_mercadoria', 'tipo_de_usuario']



class CustomLoginSerializer(LoginSerializer):
    username=None
    
    class Meta:
        model = Usuario
        fields = ['id','nome','email','sobrenome','endereco','telefone','nif','especializacao','tipo_veiculo','capacidade_do_armazem','tipo_mercadoria', 'tipo_de_usuario']



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
    #esta variavel mostra apenas os nomes e a outra é para selecionar
    id_do_fornecedor_nome = serializers.SerializerMethodField()
    id_do_fornecedor = serializers.PrimaryKeyRelatedField(queryset=Registrar_Fornecedor_mercadoria.objects.all())

    #esta variavel mostra apenas os nomes e a outra é para selecionar
    id_da_categoria_produto_nomes = serializers.SerializerMethodField()
    id_da_categoria_produto = serializers.PrimaryKeyRelatedField(many=True, queryset=Categoria.objects.all())

    #esta variavel mostra apenas os nomes e a outra é para selecionar
    id_do_produto_nomes = serializers.SerializerMethodField()
    id_do_produto = serializers.PrimaryKeyRelatedField(many=True, queryset=Produto.objects.all())

   
    class Meta:
            model = Submeter_Factura
            fields = ['id','descricao','total_pago','data_da_compra', 'id_da_categoria_produto_nomes' ,'id_da_categoria_produto', 'id_do_produto_nomes' ,'id_do_produto', 'id_do_fornecedor_nome' ,'id_do_fornecedor','id_da_localizacao','destino_da_mercadoria_pais','destino_da_mercadoria_municipio','destino_da_mercadoria_continente', 'destino_da_mercadoria_provincia', 'peso','dimensao','marca','modelo', 'usuario','ficheiro_da_fatura']


    def get_id_do_fornecedor_nome(self, obj):
        # Aqui, você pode definir como obter o campo específico do objeto relacionado
        return obj.id_do_fornecedor.nome  
    
    #pela relação ser many to many deve se fazer um ciclo para mostra uma lista de categorias
    def get_id_da_categoria_produto_nomes(self, obj):
         return [categoria.nome for categoria in obj.id_da_categoria_produto.all()] 

    #pela relação ser many to many deve se fazer um ciclo para mostra uma lista de categorias
    def get_id_do_produto_nomes(self, obj):
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


class MenuSerializer(serializers.ModelSerializer):
    filho = serializers.SerializerMethodField()
    id_do_usuario = serializers.SerializerMethodField()

    class Meta:
          model = Menu
          fields = ['id','nome','pai', 'id_do_usuario','filho']

    def get_filho(self, obj):
        # Se o objeto não tem filhos, definir filho como None
        if obj.filho.exists():
            return MenuSerializer(obj.filho.all(), many=True).data
        return None
    
    def get_id_do_usuario(self, obj):
        # Aqui, você pode definir como obter o campo específico do objeto relacionado
        return obj.id_do_usuario.nome 
    

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
          model =TipoUsuario
          fields = ['id','nome', 'rota']
