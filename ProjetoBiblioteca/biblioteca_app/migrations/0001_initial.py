# Generated by Django 2.2.5 on 2019-09-29 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('matricula', models.AutoField(max_length=8, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='endereco email')),
                ('endereco', models.TextField(blank=True, null=True)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Uncheck to disable the account', verbose_name='Is Active')),
                ('is_admin', models.BooleanField(default=False, help_text='Give admin privileges', verbose_name='Is Admin')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Usuarios',
            },
        ),
        migrations.CreateModel(
            name='Sessao',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=200)),
                ('localizacao', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Sessoes',
            },
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=200)),
                ('sessao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca_app.Sessao')),
            ],
            options={
                'verbose_name_plural': 'Livros',
            },
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('datahora', models.DateTimeField(default=django.utils.timezone.now)),
                ('devolucao', models.DateTimeField(default=django.utils.timezone.now)),
                ('livros', models.ManyToManyField(to='biblioteca_app.Livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Emprestimos',
            },
        ),
    ]
