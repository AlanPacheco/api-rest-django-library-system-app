from rest_framework.viewsets import ModelViewSet
from biblioteca_app.models import Usuario
from biblioteca_app.models import Emprestimo
from biblioteca_app.models import Livro
from biblioteca_app.models import Sessao
from .serializers import UsuarioSerializer
from .serializers import EmprestimoSerializer
from .serializers import LivroSerializer
from .serializers import SessaoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Outras formas de permissões
# from rest_framework.permissions import IsAdminUser
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import DjangoModelPermissions

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)

class SessaoViewSet(ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
