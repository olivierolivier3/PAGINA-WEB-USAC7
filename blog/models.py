from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class Categoria(models.Model):
    nombre=models.CharField(max_length=50)  #significa que va a ser cuadro de texto
    created=models.DateTimeField(auto_now_add=True)  #guardaremos la fecha en que se creo un servicio, y sera de tipo fecha, la fecha la guarda de forma automatica
    updated=models.DateTimeField(auto_now_add=True)   #guardaremos la fecha en que se modifico un servicio, sera de tipo fecha, la fecha se guarda automaticamente

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre
    

class Post(models.Model):
    titulo=models.CharField(max_length=50)  #significa que va a ser cuadro de texto
    contenido=models.CharField(max_length=50)  #significa que va a ser cuadro de texto
    imagen=models.ImageField(upload_to="blog", null=True, blank=True)#campo para subir imagen al portal, se incluiran en la carpeta "servicios" dentro de "media"
   
    autor=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
   
    created=models.DateTimeField(auto_now_add=True)  #guardaremos la fecha en que se creo un servicio, y sera de tipo fecha, la fecha la guarda de forma automatica
    updated=models.DateTimeField(auto_now_add=True)   #guardaremos la fecha en que se modifico un servicio, sera de tipo fecha, la fecha se guarda automaticamente

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.titulo

    