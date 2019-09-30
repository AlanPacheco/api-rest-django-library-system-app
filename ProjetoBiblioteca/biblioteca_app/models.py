from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin
from django.contrib import auth


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Usuario deve ter um endereco de email')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    matricula = models.AutoField(max_length=8, primary_key=True)
    nome = models.CharField(max_length=200)
    email = models.EmailField(verbose_name='endereco email', unique=True)
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    is_active = models.BooleanField(verbose_name='Is Active', default=True, help_text='Uncheck to disable the account')
    is_admin = models.BooleanField(verbose_name='Is Admin', default=False, help_text='Give admin privileges')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.nome

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def _user_has_perm(user, perm, obj):
        for backend in auth.get_backends():
            if not hasattr(backend, 'has_perm'):
                continue
            try:
                if backend.has_perm(user, perm, obj):
                    return True
            except PermissionDenied:
                return False
        return False

    def _user_has_module_perms(user, app_label):
        for backend in auth.get_backends():
            if not hasattr(backend, 'has_module_perms'):
                continue
            try:
                if backend.has_module_perms(user, app_label):
                    return True
            except PermissionDenied:
                return False
        return False


    def has_perm(self, perm, obj=None):
        # admin ativos retorna true
        if self.is_active and self.is_admin:
            return True
        # Caso contrario, eh verificado o backend
        return self._user_has_perm(perm, obj)

    def has_module_perms(self, app_label):
        if self.is_active and self.is_admin:
            return True
        return self._user_has_module_perms(app_label)

    @property
    def is_staff(self):
        return self.is_admin

    def get_name(self):
        return self.nome


class Sessao(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200)
    localizacao = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Sessoes'

    def __str__(self):
        return self.descricao


class Livro(models.Model):
    codigo = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    sessao = models.ForeignKey(Sessao, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Livros'

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
    codigo = models.AutoField(primary_key=True)
    datahora = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    devolucao = models.DateTimeField(default=timezone.now)
    livros = models.ManyToManyField(Livro)

    class Meta:
        verbose_name_plural = 'Emprestimos'

    def __str__(self):
        return self.usuario.get_name()
