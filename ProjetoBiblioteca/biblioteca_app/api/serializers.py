from rest_framework.serializers import ModelSerializer
from biblioteca_app.models import Usuario
from biblioteca_app.models import Emprestimo
from biblioteca_app.models import Livro
from biblioteca_app.models import Sessao


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('matricula', 'nome', 'email', 'endereco', 'telefone',)

class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ('codigo', 'datahora', 'usuario', 'devolucao', 'livros',)

class SessaoSerializer(ModelSerializer):
    class Meta:
        model = Sessao
        fields = ('codigo', 'descricao', 'localizacao',)

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = ('codigo', 'titulo', 'autor', 'sessao',)
