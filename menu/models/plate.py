from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid
from menu.models.ingredient import Ingredient

class Plate(models.Model):
    """
    Modelo que representa el plato de un menú (p. ej. Pollo a la canasta).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este plato")

    title = models.CharField(max_length=200)

    ingredient = models.ManyToManyField(Ingredient, help_text="Seleccione un ingrediente para este plato")
    # ManyToManyField, porque un plato puede contener muchos ingredientes y un ingrediente puede estar en varios platos.
    # La clase Ingredient ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        """
        String que representa al objeto Book
        """
        return self.title

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Menu
        """
        return reverse('plate-details', args=[str(self.id)])


    def get_edit_url(self):
        """
        Devuelve el URL a una instancia particular de Menu
        """
        return reverse('edit-plate', args=[str(self.id)])
