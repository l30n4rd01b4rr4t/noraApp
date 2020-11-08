from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^menu/$', views.MenuListView.as_view(), name='menu'),
    url(r'^menu/(?P<pk>[-\w]+)$', views.MenuDetailView.as_view(), name='menu-detail'),
]
