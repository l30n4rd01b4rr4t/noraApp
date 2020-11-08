from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from menu.models.ingredient import Ingredient

class Plate(models.Model):
    """
    Modelo que representa el plato de un menú (p. ej. Pollo a la canasta).
    """

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
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('book-detail', args=[str(self.id)])