from rest_framework import serializers
from .models import *
from rest_framework.authtoken.models import Token

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'fecha_nacimiento', 'genero', 'foto')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name')


class UserGetSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=False)
    class Meta:
        model = User
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class SubcategoriaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = '__all__'
        depth=2




class UsuarioXEventoAsistenteListEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioXEventoAsistente
        fields = ('evento', 'estado',)
        depth = 1

class UsuarioXEventoAsistenteListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuarioXEventoAsistente
        fields = ('id','usuario', 'estado', 'evento')
        depth = 2

class UsuarioXEventoAsistenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioXEventoAsistente
        fields = ('evento','usuario','estado')


#Se listan los usuarios, junto con todas sus categorías
class CategoriaListSerializer(serializers.ModelSerializer):
    subcategorias = SubcategoriaListSerializer(many=True, read_only=False)
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'foto', 'subcategorias')

##

class ComentarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('autor',)
        depth = 2


class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'




class EventoListSerializer(serializers.ModelSerializer):
    asistentes = UsuarioXEventoAsistenteListSerializer(many=True, read_only=False)
    comentarios = ComentarioListSerializer(many=True, read_only=False)
    class Meta:
        model = Evento
        fields = ('categoria','fecha', 'lugar', 'descripcion', 'imagen', 'calificacion', 'persona', 'asistentes', 'comentarios')
        depth=2

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'
        

class EventoXGrupoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoXGrupo
        fields = ('evento',)
        depth = 1

    


class UsuarioXGrupoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsuarioXGrupo
        fields = ('usuario',)
        depth = 1



class EventoXGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventoXGrupo
        fields = ('evento','grupo')


class UsuarioXGrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioXGrupo
        fields = ('usuario','grupo')


class GrupoListSerializer(serializers.ModelSerializer):
    eventosgrupo = EventoXGrupoListSerializer(many=True, read_only=False)
    usuariosgrupo = UsuarioXGrupoListSerializer(many=True, read_only=False)
    class Meta:
        model = Grupo
        fields = ('nombre', 'descripcion', 'eventosgrupo', 'usuariosgrupo', 'categoria')
        depth = 2


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'



    



class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'


class CategoriaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaUsuario
        fields = '__all__'

class CategoriaUsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaUsuario
        fields = ('categoria', 'usuario')
        depth = 2

class SubcategoriaUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcategoriaUsuario
        fields = '__all__'

class SubcategoriaUsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcategoriaUsuario
        fields = ('subcategoria',)
        depth = 2



class UsuarioListSerializer(serializers.ModelSerializer):
    eventos = EventoSerializer(many=True, read_only=False)
    miembroaventos = UsuarioXEventoAsistenteListEventSerializer(many=True, read_only = False)
    categoriasusuario = CategoriaUsuarioListSerializer(many=True, read_only=False)
    subcategoriasusuario = SubcategoriaUsuarioListSerializer(many=True, read_only=False)
    grupos = GrupoListSerializer(many=True, read_only=False)
    
    class Meta:
        model = Usuario
        fields = ('id', 'nombre', 'fecha_nacimiento', 'genero', 'foto',  'eventos', 'miembroaventos', 'categoriasusuario', 'subcategoriasusuario', 'grupos', 'user')
        depth = 1



class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'