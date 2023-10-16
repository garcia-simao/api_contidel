
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers
from core.views import UsuarioViewSet
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 
from dj_rest_auth.views import LoginView , PasswordResetView, PasswordResetConfirmView

from core.views import LoginView



router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('dj-rest-auth/login/', LoginView.as_view(), name='custom-login')

]

