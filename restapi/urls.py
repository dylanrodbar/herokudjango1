from django.conf.urls import url, include
from rest_framework import routers
from . import views

app_name = "restapi"

#router = routers.DefaultRouter()
#router.register(r'current', views.UserViewSet, base_name='api')

urlpatterns = [
    #url(r'^api/', include(router.urls)),

    url(r'^api/usuarios/listar', views.UsuarioListAPIView.as_view(), name="listar"),
    url(r'^api/usuarios/crear', views.UsuarioCreateAPIView.as_view(), name="crear"),
    url(r'^api/usuarios/(?P<pk>\d+)/detalle', views.UsuarioDetailAPIView.as_view(), name="detalle"),
    url(r'^api/usuarios/(?P<pk>\d+)/editar', views.UsuarioUpdateAPIView.as_view(), name="editar"),
    url(r'^api/usuarios/(?P<pk>\d+)/eliminar', views.UsuarioDestroyAPIView.as_view(), name="eliminar"),

    url(r'^api/categorias/listar', views.CategoriaListAPIView.as_view(), name="listar"),
    url(r'^api/categorias/crear', views.CategoriaCreateAPIView.as_view(), name="crear"),
    url(r'^api/categorias/(?P<pk>\d+)/detalle', views.CategoriaDetailAPIView.as_view(), name="detalle"),
    url(r'^api/categorias/(?P<pk>\d+)/editar', views.CategoriaUpdateAPIView.as_view(), name="editar"),
    url(r'^api/categorias/(?P<pk>\d+)/eliminar', views.CategoriaDestroyAPIView.as_view(), name="eliminar"),

    url(r'^api/subcategorias/listar', views.SubcategoriaListAPIView.as_view(), name="listar"),
    url(r'^api/subcategorias/crear', views.SubcategoriaCreateAPIView.as_view(), name="crear"),
    url(r'^api/subcategorias/(?P<pk>\d+)/detalle', views.SubcategoriaDetailAPIView.as_view(), name="detalle"),
    url(r'^api/subcategorias/(?P<pk>\d+)/editar', views.SubcategoriaUpdateAPIView.as_view(), name="editar"),
    url(r'^api/subcategorias/(?P<pk>\d+)/eliminar', views.SubcategoriaDestroyAPIView.as_view(), name="eliminar"),

    url(r'^api/tipos/listar', views.TipoListAPIView.as_view(), name="listar"),
    url(r'^api/tipos/crear', views.TipoCreateAPIView.as_view(), name="crear"),
    url(r'^api/tipos/(?P<pk>\d+)/detalle', views.TipoDetailAPIView.as_view(), name="detalle"),
    url(r'^api/tipos/(?P<pk>\d+)/editar', views.TipoUpdateAPIView.as_view(), name="editar"),
    url(r'^api/tipos/(?P<pk>\d+)/eliminar', views.TipoDestroyAPIView.as_view(), name="eliminar"),

    url(r'^api/comentarios/listar', views.ComentarioListAPIView.as_view(), name="listar"),
    url(r'^api/comentarios/crear', views.ComentarioCreateAPIView.as_view(), name="crear"),
    url(r'^api/comentarios/(?P<pk>\d+)/detalle', views.ComentarioDetailAPIView.as_view(), name="detalle"),
    url(r'^api/comentarios/(?P<pk>\d+)/editar', views.ComentarioUpdateAPIView.as_view(), name="editar"),
    url(r'^api/comentarios/(?P<pk>\d+)/eliminar', views.ComentarioDestroyAPIView.as_view(), name="eliminar"),


    url(r'^api/eventos/listar', views.EventoListAPIView.as_view(), name="listar"),
    url(r'^api/eventos/crear', views.EventoCreateAPIView.as_view(), name="crear"),
    url(r'^api/eventos/(?P<pk>\d+)/detalle', views.EventoDetailAPIView.as_view(), name="detalle"),
    url(r'^api/eventos/(?P<pk>\d+)/editar', views.EventoUpdateAPIView.as_view(), name="editar"),
    url(r'^api/eventos/(?P<pk>\d+)/eliminar', views.EventoDestroyAPIView.as_view(), name="eliminar"),

    url(r'^api/grupos/listar', views.GrupoListAPIView.as_view(), name="listar"),
    url(r'^api/grupos/crear', views.GrupoCreateAPIView.as_view(), name="crear"),
    url(r'^api/grupos/(?P<pk>\d+)/detalle', views.GrupoDetailAPIView.as_view(), name="detalle"),
    url(r'^api/grupos/(?P<pk>\d+)/editar', views.GrupoUpdateAPIView.as_view(), name="editar"),
    url(r'^api/grupos/(?P<pk>\d+)/eliminar', views.GrupoDestroyAPIView.as_view(), name="eliminar"),


    url(r'^api/usuarioevento/listar', views.UsuarioXEventoAsistenteListAPIView.as_view(), name="listar"),
    url(r'^api/usuarioevento/crear', views.UsuarioXEventoAsistenteCreateAPIView.as_view(), name="crear"),
    url(r'^api/usuarioevento/(?P<pk>\d+)/detalle', views.UsuarioXEventoAsistenteDetailAPIView.as_view(), name="detalle"),
    url(r'^api/usuarioevento/(?P<pk>\d+)/editar', views.UsuarioXEventoAsistenteUpdateAPIView.as_view(), name="editar"),
    url(r'^api/usuarioevento/(?P<pk>\d+)/eliminar', views.UsuarioXEventoAsistenteDestroyAPIView.as_view(), name="eliminar"),


    url(r'^api/usuariogrupo/listar', views.UsuarioXGrupoListAPIView.as_view(), name="listar"),
    url(r'^api/usuariogrupo/crear', views.UsuarioXGrupoCreateAPIView.as_view(), name="crear"),
    url(r'^api/usuariogrupo/(?P<pk>\d+)/detalle', views.UsuarioXGrupoDetailAPIView.as_view(), name="detalle"),
    url(r'^api/usuariogrupo/(?P<pk>\d+)/editar', views.UsuarioXGrupoUpdateAPIView.as_view(), name="editar"),
    url(r'^api/usuariogrupo/(?P<pk>\d+)/eliminar', views.UsuarioXGrupoDestroyAPIView.as_view(), name="eliminar"),

    
    url(r'^api/eventogrupo/listar', views.EventoXGrupoListAPIView.as_view(), name="listar"),
    url(r'^api/eventogrupo/crear', views.EventoXGrupoCreateAPIView.as_view(), name="crear"),
    url(r'^api/eventogrupo/(?P<pk>\d+)/detalle', views.EventoXGrupoDetailAPIView.as_view(), name="detalle"),
    url(r'^api/eventogrupo/(?P<pk>\d+)/editar', views.EventoXGrupoUpdateAPIView.as_view(), name="editar"),
    url(r'^api/eventogrupo/(?P<pk>\d+)/eliminar', views.EventoXGrupoDestroyAPIView.as_view(), name="eliminar"),

    url(r'^api/categoriausuario/listar', views.CategoriaUsuarioListAPIView.as_view(), name="listar"),
    url(r'^api/categoriausuario/crear', views.CategoriaUsuarioCreateAPIView.as_view(), name="crear"),
    url(r'^api/categoriausuario/(?P<pk>\d+)/detalle', views.CategoriaUsuarioDetailAPIView.as_view(), name="detalle"),
    url(r'^api/categoriausuario/(?P<pk>\d+)/editar', views.CategoriaUsuarioUpdateAPIView.as_view(), name="editar"),
    url(r'^api/categoriausuario/(?P<pk>\d+)/eliminar', views.CategoriaUsuarioDestroyAPIView.as_view(), name="eliminar"),
    url(r'^api/categoriausuario/id', views.CategoriaUsuarioListIdAPIView.as_view(), name="listar"),

    url(r'^api/subcategoriausuario/listar', views.SubcategoriaUsuarioListAPIView.as_view(), name="listar"),
    url(r'^api/subcategoriausuario/crear', views.SubcategoriaUsuarioCreateAPIView.as_view(), name="crear"),
    url(r'^api/subcategoriausuario/(?P<pk>\d+)/detalle', views.SubcategoriaUsuarioDetailAPIView.as_view(), name="detalle"),
    url(r'^api/subcategoriausuario/(?P<pk>\d+)/editar', views.SubcategoriaUsuarioUpdateAPIView.as_view(), name="editar"),
    url(r'^api/subcategoriausuario/(?P<pk>\d+)/eliminar', views.SubcategoriaUsuarioDestroyAPIView.as_view(), name="eliminar"),

    url(r'^api/usuarioevento/asistir', views.UsuarioXEventoAsistenteEventosAsistirAPIView.as_view(),name="asistir"),
    url(r'^api/usuarioevento/interesado', views.UsuarioXEventoAsistenteEventosInteresadoAPIView.as_view(),name="pendiente"),
    url(r'^api/usuarioevento/asistio', views.UsuarioXEventoAsistenteEventosAsistioAPIView.as_view(),name="asistio"),

    url(r'^api/eventocerca', views.EventoCercaCreateAPIView.as_view(),name="eventocer"),

    url(r'^api/ecercacategoria', views.EventoCercaCategoriaCreateAPIView.as_view(), name="asistio"),

    url(r'^api/usuarioevento/obtenerEvento', views.UsuarioXEventoAsistenteEventosObtenerAPIView.as_view(),name="eventoobtener"),
    url(r'^api/user/get', views.UserGetAPIView.as_view(),name="eventoobtener"),

    url(r'^api/editusuario', views.EditUsuarioAPIView.as_view(),name="editUsuario"),

    
    url(r'^api/usuarioactual', views.UserGetTokenAPIView.as_view(),name="eventoobtener"),

    url(r'^api/grupos/categoria', views.GrupoListCategoriaAPIView.as_view(),name="eventoobtener"),

    url(r'^api/eventos/categoria', views.EventoListCategoriaAPIView.as_view(),name="eventoobtener"),



]