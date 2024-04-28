# Criar um arquivo igual o 'urls.py' do projeto
from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('update', views.update, name='update'),
    path('delete', views.delete, name='delete'),
    path('list', views.list, name='list'),
    path('accessLevel', views.accessLevel, name='accessLevel'),
    path('published', views.published, name='published'),
    path('profile', views.profile, name='profile')
]

