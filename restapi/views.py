from django.db.models import Q
from django.shortcuts import render
from requests import Response
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.fields import CurrentUserDefault
from rest_framework.authtoken.models import Token

import geopy.distance

from rest_framework.generics import(
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    CreateAPIView
)
from rest_framework.views import APIView

from .serializer import *
from .models import *


#####
def ordenar(matriz):
    matriz.sort(key=lambda row: row[1:], reverse=False)
    nuevaMatriz = []
    for i in matriz:
        nuevaMatriz.append(i[0])
    return nuevaMatriz

#####



#restapi/api/user/get
class UserGetAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserGetSerializer

    def get_queryset(self):
        idUsuario = self.request.query_params.get('user', None)
        #usuarioE = Usuario.objects.filter(pk=idUsuario)
        #usuarioEE = usuarioE.first()
        return User.objects.filter(pk=idUsuario)


#restapi/api/editusuario
class EditUsuarioAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        idUsuario = self.request.query_params.get('user', None)
        foto = self.request.query_params.get('foto', None)
        nombre = self.request.query_params.get('nombre', None)

        usuario = Usuario.objects.filter(pk=idUsuario)
        usuario.foto = foto
        usuario.nombre = nombre
        #usuarioE = Usuario.objects.filter(pk=idUsuario)
        #usuarioEE = usuarioE.first()
        return usuario
        #return User.objects.filter(pk=idUsuario)


class UserGetTokenAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = TokenSerializer

    def get_queryset(self):
        tok = self.request.query_params.get('user', None)
        print(tok)
        user = Token.objects.filter(key=tok)
        #print(user.token)
        #print(user)
        #usuarioE = Usuario.objects.filter(pk=idUsuario)
        #usuarioEE = usuarioE.first()
        return user




#CRUD Usuario
##################################################################



#restapi/api/usuarios/crear
class UsuarioCreateAPIView(CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#restapi/api/usuarios/listar
class UsuarioListAPIView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer

# restapi/api/usuarios/listar
class UsuarioListAPIView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer


#restapi/api/usuarios/pk/detalle
class UsuarioDetailAPIView(RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioListSerializer

#restapi/api/usuarios/pk/editar
class UsuarioUpdateAPIView(UpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

#restapi/api/usuarios/pk/eliminar
class UsuarioDestroyAPIView(DestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer





##################################################################

#CRUD Categoria
##################################################################

#restapi/api/categorias/crear
class CategoriaCreateAPIView(CreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#restapi/api/categorias/listar
class CategoriaListAPIView(ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaListSerializer

#restapi/api/categorias/pk/detalle
class CategoriaDetailAPIView(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaListSerializer

#restapi/api/categorias/pk/editar
class CategoriaUpdateAPIView(UpdateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

#restapi/api/categorias/pk/eliminar
class CategoriaDestroyAPIView(DestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


##################################################################


#CRUD Subcategoria
##################################################################

#restapi/api/subcategorias/crear
class SubcategoriaCreateAPIView(CreateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

#restapi/api/subcategorias/listar
class SubcategoriaListAPIView(ListAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

#restapi/api/subcategorias/pk/detalle
class SubcategoriaDetailAPIView(RetrieveAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

#restapi/api/subcategorias/pk/editar
class SubcategoriaUpdateAPIView(UpdateAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer

#restapi/api/subcategorias/pk/eliminar
class SubcategoriaDestroyAPIView(DestroyAPIView):
    queryset = Subcategoria.objects.all()
    serializer_class = SubcategoriaSerializer


##################################################################


#CRUD Tipo
##################################################################

#restapi/api/tipos/crear
class TipoCreateAPIView(CreateAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

#restapi/api/tipos/listar
class TipoListAPIView(ListAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

#restapi/api/tipos/pk/detalle
class TipoDetailAPIView(RetrieveAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

#restapi/api/tipos/pk/editar
class TipoUpdateAPIView(UpdateAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

#restapi/api/tipos/pk/eliminar
class TipoDestroyAPIView(DestroyAPIView):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

##################################################################


#CRUD Comentario
##################################################################

#restapi/api/comentarios/crear
class ComentarioCreateAPIView(CreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

#restapi/api/comentarios/listar
class ComentarioListAPIView(ListAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioListSerializer

#restapi/api/comentarios/pk/detalle
class ComentarioDetailAPIView(RetrieveAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

#restapi/api/comentarios/pk/editar
class ComentarioUpdateAPIView(UpdateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

#restapi/api/comentarios/pk/eliminar
class ComentarioDestroyAPIView(DestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


##################################################################


#CRUD Evento
##################################################################

#restapi/api/eventos/crear
class EventoCreateAPIView(CreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

#restapi/api/eventos/listar
class EventoListAPIView(ListAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoListSerializer

#restapi/api/eventos/pk/detalle
class EventoDetailAPIView(RetrieveAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoListSerializer

#restapi/api/eventos/pk/editar
class EventoUpdateAPIView(UpdateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

#restapi/api/eventos/pk/eliminar
class EventoDestroyAPIView(DestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


#restapi/api/eventoscerca
#Obtiene los eventos más cercanos, dadas las coordenadas
class EventoCercaCreateAPIView(ListAPIView):
    serializer_class = EventoSerializer
    print("HOLISSS")
    def get_queryset(self):
        lati = self.request.query_params.get('latitud', None)
        longi = self.request.query_params.get('longitud', None)

        eventos = Evento.objects.all()
        cercanos = []

        for e in eventos:
            lat = e.latitud
            lon = e.longitud
            coords_1 = (lati, longi)
            coords_2 = (lat, lon)
            distancia = geopy.distance.vincenty(coords_1, coords_2).km
            temporal = [e, distancia]
            cercanos.append(temporal)
        cer = ordenar(cercanos)

        listaIndices = []
        for i in cer:
            listaIndices.append(i.id)


        consulta = list(Evento.objects.filter(pk__in=listaIndices))
        consulta.sort(key=lambda t: listaIndices.index(t.pk))
        return consulta



#restapi/api/eventoscerca/categoria
#Obtiene los eventos más cercanos, dadas las coordenadas
class EventoCercaCategoriaCreateAPIView(ListAPIView):
    serializer_class = EventoSerializer
    def get_queryset(self):
        lati = self.request.query_params.get('latitud', None)
        longi = self.request.query_params.get('longitud', None)
        cate = self.request.query_params.get('categoria', None)


        categorias = Categoria.objects.filter(nombre=cate)
        categoriasQ = categorias.first()
        eventos = Evento.objects.filter(categoria=categoriasQ)
        """
        cercanos = []

        for e in eventos:
            lat = e.latitud
            lon = e.longitud
            coords_1 = (lati, longi)
            coords_2 = (lat, lon)
            distancia = geopy.distance.vincenty(coords_1, coords_2).km
            temporal = [e, distancia]
            cercanos.append(temporal)
        cer = ordenar(cercanos)

        listaIndices = []
        for i in cer:
            listaIndices.append(i.id)

        consulta = list(Evento.objects.filter(pk__in=listaIndices))
        consulta.sort(key=lambda t: listaIndices.index(t.pk))
        """
        return eventos


##################################################################



#CRUD Grupo
##################################################################

#restapi/api/s/crear
class GrupoCreateAPIView(CreateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

#restapi/api/grupos/listar
class GrupoListAPIView(ListAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoListSerializer


#restapi/api/grupos/categoria
class GrupoListCategoriaAPIView(ListAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoListSerializer

    def get_queryset(self):
        categoria = self.request.query_params.get('categoria', None)
        cate = Categoria.objects.filter(nombre=categoria)
        cateO = cate.first()
        grupo = Grupo.objects.all()
        #usuarioEE = usuarioE.first()
        #return UsuarioXEventoAsistente.objects.filter(estado = estadoE)
        #return UsuarioXEventoAsistente.objects.filter(estado=estadoE, usuario=usuarioEE)
        return grupo


#restapi/api/eventos/categoria
class EventoListCategoriaAPIView(ListAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoListSerializer

    def get_queryset(self):
        categoria = self.request.query_params.get('categoria', None)
        cate = Categoria.objects.filter(nombre=categoria)
        cateO = cate.first()
        evento = Evento.objects.filter(categoria=cateO)
        return evento

#restapi/api/grupos/pk/detalle
class GrupoDetailAPIView(RetrieveAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoListSerializer

#restapi/api/grupos/pk/editar
class GrupoUpdateAPIView(UpdateAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

#restapi/api/grupos/pk/eliminar
class GrupoDestroyAPIView(DestroyAPIView):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer


##################################################################



#CRUD UsuarioXEventoAsistente
#CRUD para los asistentes a un evento, el más importante es el agregar, donde recibe un usuario y el evento a donde asiste
##################################################################

#restapi/api/usuarioevento/crear
class UsuarioXEventoAsistenteCreateAPIView(CreateAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteSerializer

#restapi/api/usuarioevento/listar
class UsuarioXEventoAsistenteListAPIView(ListAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteListSerializer


#Obtiene los eventos para un usuario, en los que este vaya a asistir

#restapi/api/usuarioevento/asistir
class UsuarioXEventoAsistenteEventosAsistirAPIView(ListAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteListSerializer

    def get_queryset(self):
        idUsuario = self.request.query_params.get('usuario', None)
        estadoE = 'Asistir'
        usuarioE = Usuario.objects.filter(pk=idUsuario)
        usuarioEE = usuarioE.first()
        #return UsuarioXEventoAsistente.objects.filter(estado = estadoE)
        return UsuarioXEventoAsistente.objects.filter(estado=estadoE, usuario=usuarioEE)

#Obtiene los eventos para un usuario, en los que este vaya a asistir

#restapi/api/usuarioevento/interesado
class UsuarioXEventoAsistenteEventosInteresadoAPIView(ListAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteListSerializer

    def get_queryset(self):
        idUsuario = self.request.query_params.get('usuario', None)
        estadoE = 'Interesado'
        usuarioE = Usuario.objects.filter(pk=idUsuario)
        usuarioEE = usuarioE.first()
        #return UsuarioXEventoAsistente.objects.filter(estado = estadoE)
        return UsuarioXEventoAsistente.objects.filter(estado=estadoE, usuario=usuarioEE)


#Obtiene los eventos para un usuario, en los que este vaya a asistir

#restapi/api/usuarioevento/asistio
class UsuarioXEventoAsistenteEventosAsistioAPIView(ListAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteListSerializer

    def get_queryset(self):
        idUsuario = self.request.query_params.get('usuario', None)
        estadoE = 'Asistió'
        usuarioE = Usuario.objects.filter(pk=idUsuario)
        usuarioEE = usuarioE.first()
        #return UsuarioXEventoAsistente.objects.filter(estado = estadoE)
        return UsuarioXEventoAsistente.objects.filter(estado=estadoE, usuario=usuarioEE)






#restapi/api/usuarioevento/obtenerEvento
#Obtiene un evento, dado un evento y un usuario, esto ayudará a obtener su id y luego cambiar si un usuario pasa, por ejemplo, de asistir a un evento a interesado
class UsuarioXEventoAsistenteEventosObtenerAPIView(ListAPIView):
    #queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteListSerializer

    def get_queryset(self):
        idEvento = self.request.query_params.get('evento', None)
        idUsuario = self.request.query_params.get('usuario', None)

        usuL = Usuario.objects.filter(pk=idUsuario)
        eveL = Evento.objects.filter(pk=idEvento)

        usu = usuL.first()
        eve = eveL.first()
        return UsuarioXEventoAsistente.objects.filter(evento = eve, usuario=usu)



#restapi/api/usuarioevento/pk/detalle
class UsuarioXEventoAsistenteDetailAPIView(RetrieveAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteListSerializer

#restapi/api/usuarioevento/pk/editar
class UsuarioXEventoAsistenteUpdateAPIView(UpdateAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteSerializer

#restapi/api/usuarioevento/pk/eliminar
class UsuarioXEventoAsistenteDestroyAPIView(DestroyAPIView):
    queryset = UsuarioXEventoAsistente.objects.all()
    serializer_class = UsuarioXEventoAsistenteSerializer



##################################################################



#CRUD UsuarioXGrupo
#El más importante es agregar un usuario a un grupo, dado el id del usuario y el id del grupo
##################################################################

#restapi/api/usuariogrupo/crear
class UsuarioXGrupoCreateAPIView(CreateAPIView):
    queryset = UsuarioXGrupo.objects.all()
    serializer_class = UsuarioXGrupoSerializer

#restapi/api/usuariogrupo/listar
class UsuarioXGrupoListAPIView(ListAPIView):
    queryset = UsuarioXGrupo.objects.all()
    serializer_class = UsuarioXGrupoListSerializer

#restapi/api/usuariogrupo/pk/detalle
class UsuarioXGrupoDetailAPIView(RetrieveAPIView):
    queryset = UsuarioXGrupo.objects.all()
    serializer_class = UsuarioXGrupoListSerializer

#restapi/api/usuariogrupo/pk/editar
class UsuarioXGrupoUpdateAPIView(UpdateAPIView):
    queryset = UsuarioXGrupo.objects.all()
    serializer_class = UsuarioXGrupoSerializer

#restapi/api/usuariogrupo/pk/eliminar
class UsuarioXGrupoDestroyAPIView(DestroyAPIView):
    queryset = UsuarioXGrupo.objects.all()
    serializer_class = UsuarioXGrupoSerializer



##################################################################


#CRUD EventoXGrupo
#El más  importante es agregar un evento a un grupo, dado un id de evento y un id de grupo
##################################################################

#restapi/api/eventogrupo/crear
class EventoXGrupoCreateAPIView(CreateAPIView):
    queryset = EventoXGrupo.objects.all()
    serializer_class = EventoXGrupoSerializer

#restapi/api/eventogrupo/listar
class EventoXGrupoListAPIView(ListAPIView):
    queryset = EventoXGrupo.objects.all()
    serializer_class = EventoXGrupoListSerializer

#restapi/api/eventogrupo/pk/detalle
class EventoXGrupoDetailAPIView(RetrieveAPIView):
    queryset = EventoXGrupo.objects.all()
    serializer_class = EventoXGrupoListSerializer

#restapi/api/eventogrupo/pk/editar
class EventoXGrupoUpdateAPIView(UpdateAPIView):
    queryset = EventoXGrupo.objects.all()
    serializer_class = EventoXGrupoSerializer

#restapi/api/eventogrupo/pk/eliminar
class EventoXGrupoDestroyAPIView(DestroyAPIView):
    queryset = EventoXGrupo.objects.all()
    serializer_class = EventoXGrupoSerializer



##################################################################


#CRUD CategoriaUsuario
#Categorias para el usuario
##################################################################

#restapi/api/categoriausuario/crear
class CategoriaUsuarioCreateAPIView(CreateAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioSerializer

#restapi/api/categoriausuario/listar
class CategoriaUsuarioListAPIView(ListAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioListSerializer


#restapi/api/categoriausuario/id
class CategoriaUsuarioListIdAPIView(ListAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioListSerializer

    def get_queryset(self):
        idUsuario = self.request.query_params.get('usuario', None)

        usuL = Usuario.objects.filter(pk=idUsuario)

        usu = usuL.first()
        return CategoriaUsuario.objects.filter(usuario=usu)


#restapi/api/categoriausuario/pk/detalle
class CategoriaUsuarioDetailAPIView(RetrieveAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioListSerializer

#restapi/api/categoriausuario/pk/editar
class CategoriaUsuarioUpdateAPIView(UpdateAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioSerializer

#restapi/api/categoriausuario/pk/eliminar
class CategoriaUsuarioDestroyAPIView(DestroyAPIView):
    queryset = CategoriaUsuario.objects.all()
    serializer_class = CategoriaUsuarioSerializer



##################################################################



#CRUD SubcategoriaUsuario
#Subcategorias para el usuario
##################################################################

#restapi/api/subcategoriausuario/crear
class SubcategoriaUsuarioCreateAPIView(CreateAPIView):
    queryset = SubcategoriaUsuario.objects.all()
    serializer_class = SubcategoriaUsuarioSerializer

#restapi/api/subcategoriausuario/listar
class SubcategoriaUsuarioListAPIView(ListAPIView):
    queryset = SubcategoriaUsuario.objects.all()
    serializer_class = SubcategoriaUsuarioListSerializer

#restapi/api/subcategoriausuario/pk/detalle
class SubcategoriaUsuarioDetailAPIView(RetrieveAPIView):
    queryset = SubcategoriaUsuario.objects.all()
    serializer_class = SubcategoriaUsuarioListSerializer

#restapi/api/subcategoriausuario/pk/editar
class SubcategoriaUsuarioUpdateAPIView(UpdateAPIView):
    queryset = SubcategoriaUsuario.objects.all()
    serializer_class = SubcategoriaUsuarioSerializer

#restapi/api/subcategoriausuario/pk/eliminar
class SubcategoriaUsuarioDestroyAPIView(DestroyAPIView):
    queryset = SubcategoriaUsuario.objects.all()
    serializer_class = SubcategoriaUsuarioSerializer



##################################################################




class CurrentUserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)