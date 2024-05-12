from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title=models.CharField(verbose_name="Titulo", max_length=200)
    content=RichTextField(verbose_name="Contenido")
    # sirve para crear un editor de texto en el admin, hay que instalar el paquete ckeditor y agregarlo a install_apps,
    # tambien al final de installed_apps se puede editar que quiere uno que aparezca, sino se pone nada aparece todo
    order=models.SmallIntegerField(verbose_name="Orden", default=0)
        # Sirve para acomodar el orden de los campos en el admin,
        # desp de crear orden hay que agregarlo en el admyn.py,
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de edición")

    class Meta:
        verbose_name="página"
        verbose_name_plural="páginas"
        ordering=["order", "title"]

    def __str__(self):
        return self.title