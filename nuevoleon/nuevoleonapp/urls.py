# nuevoleonapp/urls.py
# nuevoleonapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('index/', views.index, name='index'),
    path('coahuila/', views.coahuila_view, name='coahuila'),
    path('sanluis/', views.sanluis_view, name='sanluis'),
    path('zacatecas/', views.zacatecas_view, name='zacatecas'),
    path('datos/', views.datos_view, name='datos'),# Ruta para la página principal
]

