from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid
from menu.models.plate import Plate

class Menu(models.Model):
    """
    Modelo que representa el menú (p. ej. Menú del día 01/01/2000).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este menu")

    title = models.CharField(max_length=200)

    plate = models.ManyToManyField(Plate, help_text="Seleccione un plato para este menu")
    # ManyToManyField, porque un menu puede contener muchos platos y un plato puede estar en varios menus.
    # La clase Plate ya ha sido definida, entonces podemos especificar el objeto arriba.

    date = models.DateField(null=True, blank=True)
    # ManyToManyField, porque un menu puede contener muchos platos y un plato puede estar en varios menus.
    # La clase Plate ya ha sido definida, entonces podemos especificar el objeto arriba.

    def __str__(self):
        """
        String que representa al objeto Menu
        """
        return self.title


    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Menu
        """
        return reverse('menu-detail', args=[str(self.id)])

    def get_edit_url(self):
        """
        Devuelve el URL a una instancia particular de Menu
        """
        return reverse('edit-menu', args=[str(self.id)])
