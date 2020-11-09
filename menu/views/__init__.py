from menu.views.index import index
from menu.views.login import login
from menu.views.logout import logout
from menu.views.register import register
from menu.models.ingredient import Ingredient
from menu.models.plate import Plate
from menu.models.menu import Menu
from django.views import generic

__all__ = [
    'index',
    'login',
    'logout',
    'register',
]

class IngredientCreate(generic.CreateView):
    model = Ingredient
    fields = ['name']
    success_url = 'ingredient-list'

class IngredientListView(generic.ListView):
    model = Ingredient

class IngredientUpdate(generic.UpdateView):
    model = Ingredient
    fields = ['name']
    template_name_suffix = '_update_form'
    success_url = '/menu/ingredient-list'

class PlateCreate(generic.CreateView):
    model = Plate
    fields = ['title', 'ingredient']
    success_url = 'plate-list'

class PlateDetailView(generic.DetailView):
    model = Plate

class PlateUpdate(generic.UpdateView):
    model = Plate
    fields = ['title', 'ingredient']
    template_name_suffix = '_update_form'
    success_url = '/menu/plate-list'

class PlateListView(generic.ListView):
    model = Plate

class MenuCreate(generic.CreateView):
    model = Menu
    fields = ['title', 'plate', 'date']
    success_url = 'menu-list'

class MenuListView(generic.ListView):
    model = Menu

class MenuDetailView(generic.DetailView):
    model = Menu

class MenuUpdate(generic.UpdateView):
    model = Menu
    fields = ['title', 'plate', 'date']
    template_name_suffix = '_update_form'
    success_url = '/menu/menu-list'
