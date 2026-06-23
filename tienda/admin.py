from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from django.utils.html import format_html
from unfold.admin import ModelAdmin, TabularInline
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import Categoria, SubCategoria, Producto

# Ocultar "Sitios" (django.contrib.sites) del panel de administración.
admin.site.unregister(Site)

# Re-registrar Usuarios y Grupos con el ModelAdmin de Unfold para que se vean
# con el tema y muestren correctamente sus controles (incluido el botón de
# "Agregar usuario"). El admin por defecto de Django no rinde con Unfold.
admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


class SubCategoriaInline(TabularInline):
    model = SubCategoria
    extra = 0


@admin.register(Categoria)
class CategoriaAdmin(ModelAdmin):
    list_display = ['nombre', 'icono', 'orden']
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [SubCategoriaInline]


@admin.register(SubCategoria)
class SubCategoriaAdmin(ModelAdmin):
    list_display = ['nombre', 'categoria', 'orden']
    list_filter = ['categoria']
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Producto)
class ProductoAdmin(ModelAdmin):
    list_display = ['miniatura', 'codigo', 'nombre', 'subcategoria', 'material', 'acabado', 'destacado']
    list_display_links = ['codigo', 'nombre']
    list_filter = ['subcategoria__categoria', 'material', 'acabado', 'destacado']
    search_fields = ['nombre', 'codigo', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['destacado']
    readonly_fields = ['vista_previa']
    fields = [
        'subcategoria', 'codigo', 'nombre', 'slug', 'descripcion',
        'material', 'acabado', 'norma', 'grado',
        'vista_previa', 'imagen',
        'destacado', 'activo',
    ]

    @admin.display(description='Imagen')
    def miniatura(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="height:40px;width:40px;object-fit:contain;border-radius:4px;" />',
                obj.imagen.url,
            )
        return '—'

    @admin.display(description='Vista previa')
    def vista_previa(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="max-height:200px;max-width:100%;object-fit:contain;border-radius:6px;" />',
                obj.imagen.url,
            )
        return 'Sin imagen'
