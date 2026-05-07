from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/<slug:slug>/', views.categoria_detalle, name='categoria'),
    path('catalogo/<slug:cat_slug>/<slug:sub_slug>/', views.subcategoria_detalle, name='subcategoria'),
    path('producto/<str:codigo>/', views.producto_detalle, name='producto'),
    path('seguridad-industrial/', views.seguridad_industrial, name='seguridad_industrial'),
]
