from django.contrib import admin

from .models import Categoria, SubCategoria, Producto


class SubCategoriaInline(admin.TabularInline):
    model = SubCategoria
    extra = 0


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'icono', 'orden']
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [SubCategoriaInline]


@admin.register(SubCategoria)
class SubCategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'orden']
    list_filter = ['categoria']
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'subcategoria', 'material', 'acabado', 'destacado']
    list_filter = ['subcategoria__categoria', 'material', 'acabado', 'destacado']
    search_fields = ['nombre', 'codigo', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['destacado']
