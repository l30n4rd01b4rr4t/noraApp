from django.shortcuts import render, redirect
from menu.models import Menu

def index(request):
    """
    Función vista para la página inicio del sitio.
    """

    # Si NO estamos identificados lo devolvemos al login
    if request.user.is_authenticated is not True:
        return redirect('login')

    # Genera contadores de algunos de los objetos principales
    num_menu=Menu.objects.count()

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_menu':num_menu},
    )
