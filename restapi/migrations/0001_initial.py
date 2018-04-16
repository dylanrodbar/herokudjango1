# Generated by Django 2.0.4 on 2018-04-16 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
                ('foto', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('lugar', models.TextField(max_length=100)),
                ('descripcion', models.TextField(max_length=1000)),
                ('imagen', models.TextField(max_length=1000)),
                ('calificacion', models.DecimalField(decimal_places=1, max_digits=2)),
                ('latitud', models.TextField(max_length=30)),
                ('longitud', models.TextField(max_length=30)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='EventoXGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Evento')),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('descripcion', models.TextField(max_length=1000)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
                ('foto', models.TextField(max_length=1000)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategorias', to='restapi.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='SubcategoriaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Subcategoria')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField(default='2017-01-01')),
                ('genero', models.TextField(default='', max_length=20, null=True)),
                ('foto', models.TextField(max_length=1000)),
                ('nombre', models.TextField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCategoriaSubcategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategoriasU', to='restapi.Categoria')),
                ('subcategoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Subcategoria')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriasU', to='restapi.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioXEventoAsistente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.TextField(max_length=20)),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistentes', to='restapi.Evento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='miembroaventos', to='restapi.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioXGrupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuariosgrupo', to='restapi.Grupo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restapi.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='subcategoriausuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategoriasusuario', to='restapi.Usuario'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grupos', to='restapi.Usuario'),
        ),
        migrations.AddField(
            model_name='eventoxgrupo',
            name='grupo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventosgrupo', to='restapi.Grupo'),
        ),
        migrations.AddField(
            model_name='evento',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='restapi.Usuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(max_length=45, on_delete=django.db.models.deletion.CASCADE, related_name='autorC', to='restapi.Usuario'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='restapi.Evento'),
        ),
        migrations.AddField(
            model_name='categoriausuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriasusuario', to='restapi.Usuario'),
        ),
    ]
