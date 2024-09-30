from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo=models.CharField(max_length=50)  #significa que va a ser cuadro de texto
    contenido=models.CharField(max_length=500)  #significa que va a ser cuadro de texto
    imagen=models.ImageField(upload_to='servicios')#campo para subir imagen al portal, se incluiran en la carpeta "servicios" dentro de "media"
    created=models.DateTimeField(auto_now_add=True)  #guardaremos la fecha en que se creo un servicio, y sera de tipo fecha, la fecha la guarda de forma automatica
    updated=models.DateTimeField(auto_now_add=True)   #guardaremos la fecha en que se modifico un servicio, sera de tipo fecha, la fecha se guarda automaticamente

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
    
    def __str__(self):
        return self.titulo

