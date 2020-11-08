from menu.views.index import index
from menu.views.login import login
from menu.views.logout import logout
from menu.views.register import register

from menu.models import Menu
from django.views import generic

__all__ = [ 
    'index',
    'login',
    'logout',
    'register',
]

class MenuListView(generic.ListView):
    model = Menu

class MenuDetailView(generic.DetailView):
    model = Menu