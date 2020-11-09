from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^create-menu$', views.MenuCreate.as_view(), name='create-menu'),
    url(r'^menu-list/$', views.MenuListView.as_view(), name='menu-list'),
    url(r'^menu/(?P<pk>[-\w]+)$', views.MenuDetailView.as_view(), name='menu-detail'),
    url(r'^edit-menu/(?P<pk>[-\w]+)$', views.MenuUpdate.as_view(), name='edit-menu'),
    url(r'^create-ingredient$', views.IngredientCreate.as_view(), name='create-ingredient'),
    url(r'^ingredient-list/$', views.IngredientListView.as_view(), name='ingredient-list'),
    url(r'^edit-ingredient/(?P<pk>[-\w]+)$', views.IngredientUpdate.as_view(), name='edit-ingredient'),
    url(r'^create-plate$', views.PlateCreate.as_view(), name='create-plate'),
    url(r'^plate-list/$', views.PlateListView.as_view(), name='plate-list'),
    url(r'^plate-details/(?P<pk>[-\w]+)$', views.PlateDetailView.as_view(), name='plate-details'),
    url(r'^edit-plate/(?P<pk>[-\w]+)$', views.PlateUpdate.as_view(), name='edit-plate'),
]
