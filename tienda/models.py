from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="CategoriaCursos"
        verbose_name_plural="CategoriasCursos"

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.TextField()
    categorias=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)#el ForeignKey se usa para enlazar un parametro de clase con otra clase.
    imagen=models.ImageField(upload_to="tienda", null=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)




    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"
