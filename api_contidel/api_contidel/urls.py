
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from dj_rest_auth.views import PasswordResetView 
from core.views import CustomLoginView, CustomPasswordResetConfirmView
from django.conf import settings
from django.conf.urls.static import static

from core.views import UsuarioViewSet
from core.views import Registrar_Certificado_Camara_ComercioViewSet
from core.views import Registrar_Fornecedor_mercadoriaViewSet
from core.views import Registrar_Localizacao_mercadoriaViewSet
from core.views import Submeter_FacturaViewSet
from core.views import CategoriaViewSet
from core.views import ProdutoViewSet


from core.views import ContinenteViewSet
from core.views import PaisViewSet
from core.views import ProvinciaViewSet
from core.views import MunicipioViewSet


router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)
router.register(r'comprador-registrar-certificado', Registrar_Certificado_Camara_ComercioViewSet)
router.register(r'comprador-registrar-fornecedor', Registrar_Fornecedor_mercadoriaViewSet)
router.register(r'comprador-registrar-localizacao', Registrar_Localizacao_mercadoriaViewSet)
router.register(r'comprador-submeter-factura', Submeter_FacturaViewSet)
router.register(r'categoria', CategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)

router.register(r'continente', ContinenteViewSet)
router.register(r'pais', PaisViewSet)
router.register(r'provincia', ProvinciaViewSet)
router.register(r'municipio', MunicipioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('dj-rest-auth/login/', CustomLoginView.as_view(), name='custom-login'),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('dj-rest-auth/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('dj-rest-auth/password/reset/confirm/<str:uidb64>/<str:token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

