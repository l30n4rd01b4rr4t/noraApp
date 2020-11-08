from django.shortcuts import redirect

from django.contrib.auth import logout as do_logout

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('login')