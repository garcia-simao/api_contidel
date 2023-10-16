from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.db.models.signals import post_save






class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O campo de e-mail é obrigatório.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superusuário deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superusuário deve ter is_superuser=True.')

        return self.create_user(email, password, **extra_fields)



class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=150, blank=True)
    sobrenome = models.CharField(max_length=150, blank=True)
    endereco = models.CharField(max_length=150, blank=True)
    telefone = models.CharField(max_length=150, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    nif = models.CharField(max_length=14, blank=True)
    especializacao = models.CharField(max_length=150, blank=True)
    tipo_veiculo = models.CharField(max_length=45, blank=True)
    capacidade_do_armazem = models.CharField(max_length=45, blank=True)
    tipo_mercadoria = models.CharField(max_length=85, blank=True)
    tipo_de_entidade = models.CharField(max_length=85, blank=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

    
    USERNAME_FIELD = 'email'

    objects= UsuarioManager()

    def __str__(self):
        return self.email
    

    def get_by_natural_key(self, email):
        return self.__class__.objects.get(email=email)
    
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super().save(*args, **kwargs)

    
    
@receiver(post_save, sender=Usuario)
def report_uploaded(sender, instance, created, **kwards):
    if created:
        Token.objects.get_or_create(user=instance)
