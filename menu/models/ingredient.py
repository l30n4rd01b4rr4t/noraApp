from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Ingredient(models.Model):
    """
    Modelo que representa un ingrediente del plato (p. ej. carne asada, arroz, etc).
    """
    name = models.CharField(max_length=200, help_text="Ingrese el nombre del ingrediente (p. ej. Pollo frito)")
    
    def __str__(self):
        """
        Cadena que representa a la instancia particular del intgrediente (p. ej. Pollo frito)
        """
        return self.name