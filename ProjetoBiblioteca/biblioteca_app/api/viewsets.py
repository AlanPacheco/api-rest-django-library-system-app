from rest_framework.viewsets import ModelViewSet
from biblioteca_app.models import Usuario
from biblioteca_app.models import Emprestimo
from biblioteca_app.models import Livro
from biblioteca_app.models import Sessao
from .serializers import UsuarioSerializer
from .serializers import EmprestimoSerializer
from .serializers import LivroSerializer
from .serializers import SessaoSerializer

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class SessaoViewSet(ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer
