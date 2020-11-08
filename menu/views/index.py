from django.shortcuts import render, redirect
from menu.models import Ingredient, Plate, Menu

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_ingredients=Ingredient.objects.all().count()
    num_plates=Plate.objects.all().count()
    num_menu=Menu.objects.count()
    
    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_ingredients':num_ingredients,'num_plates':num_plates,'num_menu':num_menu},
    )