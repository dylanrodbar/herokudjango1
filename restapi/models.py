# coding=utf-8
from django.db import models
from django.core.files.base import ContentFile
from django.contrib.auth.models import User


#Con este usuario, se autenticará dentro del api
class Usuario(models.Model):
    correo = models.TextField(max_length=30)
    contrasena = models.TextField(max_length=30)
    fecha_nacimiento = models.DateField(auto_now = False)
    genero = models.TextField(max_length=20)
    foto = models.ImageField(upload_to='Usuario', default="https://res.cloudinary.com/poppycloud/image/upload/v1/media/Usuario/dua-lipa-new-rules-christmas-920x584_jnlqqb")


class Categoria(models.Model):
    nombre = models.TextField(max_length=30)
    foto = models.ImageField(upload_to='Usuario', default="https://res.cloudinary.com/poppycloud/image/upload/v1/media/Usuario/dua-lipa-new-rules-christmas-920x584_jnlqqb")

#Las subcategorías pertenecen a una categoría
class Subcategoria(models.Model):
    nombre = models.TextField(max_length=30)
    foto = models.ImageField(upload_to='Usuario', default="https://res.cloudinary.com/poppycloud/image/upload/v1/media/Usuario/dua-lipa-new-rules-christmas-920x584_jnlqqb")
    categoria = models.ForeignKey(Categoria, related_name="subcategorias", on_delete=models.CASCADE)

#Categorías asociadas con un usuario
class CategoriaUsuario(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name="categoriasusuario", on_delete=models.CASCADE)

#Subcategorías asociadas con un usuario
class SubcategoriaUsuario(models.Model):
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name="subcategoriasusuario", on_delete=models.CASCADE)



##
class UsuarioCategoriaSubcategoria(models.Model):
    usuario = models.ForeignKey(Usuario, related_name="categoriasU", on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, related_name="subcategoriasU", on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE)
##    


class Tipo(models.Model):
    nombre = models.TextField(max_length=30)


class Evento(models.Model):
    fecha = models.DateField(auto_now=False)
    lugar = models.TextField(max_length=100)
    descripcion= models.TextField(max_length=1000)
    imagen = models.ImageField(upload_to='Usuario')
    calificacion = models.DecimalField(max_digits=2, decimal_places=1)
    persona = models.ForeignKey(Usuario, related_name="eventos", on_delete=models.CASCADE)
    latitud = models.TextField(max_length=30)
    longitud = models.TextField(max_length=30)
    

class UsuarioXEventoAsistente(models.Model):
    evento = models.ForeignKey(Evento, related_name="asistentes", on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, related_name="miembroaventos", on_delete=models.CASCADE)
    estado = models.TextField(max_length=20)


class Comentario(models.Model):
    contenido = models.TextField(max_length=1000)
    autor = models.ForeignKey(Usuario, max_length=45, related_name="autorC", on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, related_name="comentarios", on_delete=models.CASCADE)


class Grupo(models.Model):
    nombre = models.TextField(max_length=50)
    descripcion = models.TextField(max_length=1000)
    foto = models.ImageField(upload_to='Usuario', default="https://res.cloudinary.com/poppycloud/image/upload/v1/media/Usuario/dua-lipa-new-rules-christmas-920x584_jnlqqb")


class EventoXGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, related_name="eventosgrupo", on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)


class UsuarioXGrupo(models.Model):
    grupo = models.ForeignKey(Grupo, related_name="usuariosgrupo", on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
