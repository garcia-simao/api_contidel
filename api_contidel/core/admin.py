from django.contrib import admin

from .models import Usuario
from .models import Registrar_Certificado_Camara_Comercio
from .models import Registrar_Fornecedor_mercadoria
from .models import Registrar_Localizacao_mercadoria
from .models import Submeter_Factura
from .models import Categoria
from .models import Produto
from .models import Menu

from .models import Continente
from .models import Pais
from .models import Provincia
from .models import Municipio
from .models import TipoUsuario



admin.site.register(Usuario)
admin.site.register(Registrar_Certificado_Camara_Comercio)
admin.site.register(Registrar_Fornecedor_mercadoria)
admin.site.register(Registrar_Localizacao_mercadoria)
admin.site.register(Submeter_Factura)
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Menu)
admin.site.register(TipoUsuario)


admin.site.register(Continente)
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Municipio)
