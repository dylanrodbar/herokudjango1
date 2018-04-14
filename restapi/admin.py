from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Subcategoria)
admin.site.register(UsuarioCategoriaSubcategoria)
admin.site.register(Tipo)
admin.site.register(Evento)
admin.site.register(UsuarioXEventoAsistente)
admin.site.register(Comentario)
admin.site.register(Grupo)
admin.site.register(EventoXGrupo)
admin.site.register(UsuarioXGrupo)

#admin.site.register(Categoria)
