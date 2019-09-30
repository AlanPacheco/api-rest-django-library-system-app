from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm

from .models import Usuario
from .models import Sessao
from .models import Livro
from .models import Emprestimo

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmacao da Senha', widget=forms.PasswordInput,
                        help_text="Informe a mesma senha informada acima.")

    class Meta:
        model = Usuario
        fields = ('matricula','nome', 'email', 'endereco', 'telefone')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError(
                "Senhas nao correspondem",
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = '__all__'

    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('matricula','nome','email','telefone')
    list_filter = ('is_admin', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Gerenciamento de Usuarios', {'fields': ('is_admin', 'is_active',)}),
        ('Informações Pessoais', {'fields': ('nome', 'endereco', 'telefone',)}),
        ('Permissões', {'fields': ('groups','user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                 'email', 'is_admin', 'nome', 'endereco', 'telefone', 'password1', 'password2')}
         ),
         ('Permissões', {'fields': ('groups', 'user_permissions')}),
    )
    search_fields = ('email',)
    ordering = ('-matricula',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login', 'date_joined',)


admin.site.register(Usuario,UserAdmin)
admin.site.register(Sessao)
admin.site.register(Livro)
admin.site.register(Emprestimo)

# admin.site.unregister(Group)
