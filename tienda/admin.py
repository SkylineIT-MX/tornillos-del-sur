from django.contrib import admin, messages
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.sites.models import Site
from django.db.models import Count, Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import path, reverse
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


class AccionesPrecioSeccionMixin:
    """Acciones para prender/apagar los precios de secciones completas."""

    #: filtro que, dado el queryset de secciones, devuelve sus productos
    filtro_productos = None

    def _cambiar_precios(self, request, queryset, mostrar):
        productos = Producto.objects.filter(**{self.filtro_productos: queryset})
        actualizados = productos.exclude(mostrar_precio=mostrar).update(mostrar_precio=mostrar)
        verbo = 'activó' if mostrar else 'desactivó'
        extra = '' if mostrar else ' Los precios capturados se conservan.'
        self.message_user(
            request,
            f'Se {verbo} el precio de {actualizados} producto(s) '
            f'en {queryset.count()} sección(es).{extra}',
            messages.SUCCESS,
        )

    @admin.action(description='Activar precios de las secciones seleccionadas')
    def activar_precios_seccion(self, request, queryset):
        self._cambiar_precios(request, queryset, True)

    @admin.action(description='Desactivar precios de las secciones seleccionadas')
    def desactivar_precios_seccion(self, request, queryset):
        self._cambiar_precios(request, queryset, False)


@admin.register(Categoria)
class CategoriaAdmin(AccionesPrecioSeccionMixin, ModelAdmin):
    list_display = ['nombre', 'icono', 'orden']
    prepopulated_fields = {'slug': ('nombre',)}
    inlines = [SubCategoriaInline]
    actions = ['activar_precios_seccion', 'desactivar_precios_seccion']
    filtro_productos = 'subcategoria__categoria__in'


@admin.register(SubCategoria)
class SubCategoriaAdmin(AccionesPrecioSeccionMixin, ModelAdmin):
    list_display = ['nombre', 'categoria', 'orden']
    list_filter = ['categoria']
    prepopulated_fields = {'slug': ('nombre',)}
    actions = ['activar_precios_seccion', 'desactivar_precios_seccion']
    filtro_productos = 'subcategoria__in'


@admin.register(Producto)
class ProductoAdmin(ModelAdmin):
    list_display = [
        'miniatura', 'codigo', 'nombre', 'subcategoria', 'material', 'acabado',
        'precio_en_lista', 'mostrar_precio', 'destacado', 'boton_editar',
    ]
    list_display_links = ['codigo', 'nombre']
    list_filter = ['subcategoria__categoria', 'material', 'acabado', 'destacado', 'mostrar_precio']
    search_fields = ['nombre', 'codigo', 'descripcion']
    prepopulated_fields = {'slug': ('nombre',)}
    list_editable = ['mostrar_precio', 'destacado']
    readonly_fields = ['vista_previa']
    actions = ['activar_precio', 'desactivar_precio']
    fields = [
        'subcategoria', 'codigo', 'nombre', 'slug', 'descripcion',
        'material', 'acabado', 'norma', 'grado',
        'vista_previa', 'imagen',
        'precio', 'mostrar_precio',
        'destacado', 'activo',
    ]

    # --- Panel de precios (botones global y por sección) -----------------

    def get_urls(self):
        urls = [
            path(
                'precios/',
                self.admin_site.admin_view(self.precios_view),
                name='tienda_producto_precios',
            ),
        ]
        return urls + super().get_urls()

    def precios_view(self, request):
        """Página con interruptores globales y por sección para los precios."""
        if not self.has_change_permission(request):
            messages.error(request, 'No tienes permisos para modificar precios.')
            return redirect('admin:index')

        if request.method == 'POST':
            return self._aplicar_cambio_precios(request)

        productos = Producto.objects.all()
        agregados = productos.aggregate(
            total=Count('id'),
            con_precio=Count('id', filter=Q(precio__isnull=False)),
            visibles=Count('id', filter=Q(precio__isnull=False, mostrar_precio=True)),
        )

        categorias = (
            Categoria.objects.annotate(
                total=Count('subcategorias__productos', distinct=True),
                con_precio=Count(
                    'subcategorias__productos',
                    filter=Q(subcategorias__productos__precio__isnull=False),
                    distinct=True,
                ),
                visibles=Count(
                    'subcategorias__productos',
                    filter=Q(
                        subcategorias__productos__precio__isnull=False,
                        subcategorias__productos__mostrar_precio=True,
                    ),
                    distinct=True,
                ),
            )
            .prefetch_related('subcategorias')
            .order_by('orden', 'nombre')
        )

        subcategorias = (
            SubCategoria.objects.annotate(
                total=Count('productos', distinct=True),
                con_precio=Count(
                    'productos',
                    filter=Q(productos__precio__isnull=False),
                    distinct=True,
                ),
                visibles=Count(
                    'productos',
                    filter=Q(productos__precio__isnull=False, productos__mostrar_precio=True),
                    distinct=True,
                ),
            )
            .select_related('categoria')
            .order_by('categoria__orden', 'categoria__nombre', 'orden', 'nombre')
        )

        subcategorias_por_categoria = {}
        for sub in subcategorias:
            subcategorias_por_categoria.setdefault(sub.categoria_id, []).append(sub)

        secciones = [
            {'categoria': cat, 'subcategorias': subcategorias_por_categoria.get(cat.id, [])}
            for cat in categorias
        ]

        contexto = {
            **self.admin_site.each_context(request),
            'title': 'Control de precios',
            'opts': self.model._meta,
            'resumen': agregados,
            'secciones': secciones,
        }
        return render(request, 'admin/tienda/producto/precios.html', contexto)

    def _aplicar_cambio_precios(self, request):
        accion = request.POST.get('accion')
        alcance = request.POST.get('alcance')
        objeto_id = request.POST.get('objeto_id') or None

        if accion not in ('activar', 'desactivar'):
            messages.error(request, 'Acción no válida.')
            return HttpResponseRedirect(request.path)

        mostrar = accion == 'activar'
        productos = Producto.objects.all()
        etiqueta = 'todo el catálogo'

        if alcance == 'categoria':
            categoria = Categoria.objects.filter(pk=objeto_id).first()
            if categoria is None:
                messages.error(request, 'La categoría indicada ya no existe.')
                return HttpResponseRedirect(request.path)
            productos = productos.filter(subcategoria__categoria=categoria)
            etiqueta = f'la categoría «{categoria.nombre}»'
        elif alcance == 'subcategoria':
            subcategoria = SubCategoria.objects.filter(pk=objeto_id).first()
            if subcategoria is None:
                messages.error(request, 'La subcategoría indicada ya no existe.')
                return HttpResponseRedirect(request.path)
            productos = productos.filter(subcategoria=subcategoria)
            etiqueta = f'la subcategoría «{subcategoria.nombre}»'
        elif alcance != 'global':
            messages.error(request, 'Alcance no válido.')
            return HttpResponseRedirect(request.path)

        actualizados = productos.exclude(mostrar_precio=mostrar).update(mostrar_precio=mostrar)
        verbo = 'activaron' if mostrar else 'desactivaron'
        messages.success(
            request,
            f'Se {verbo} los precios de {actualizados} producto(s) en {etiqueta}. '
            'Los precios capturados se conservan.',
        )
        return HttpResponseRedirect(request.path)

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['precios_url'] = reverse('admin:tienda_producto_precios')
        return super().changelist_view(request, extra_context)

    # --- Acciones sobre la selección de la lista -------------------------

    @admin.action(description='Activar precio en los productos seleccionados')
    def activar_precio(self, request, queryset):
        actualizados = queryset.exclude(mostrar_precio=True).update(mostrar_precio=True)
        self.message_user(
            request,
            f'Se activó el precio en {actualizados} producto(s).',
            messages.SUCCESS,
        )

    @admin.action(description='Desactivar precio en los productos seleccionados')
    def desactivar_precio(self, request, queryset):
        actualizados = queryset.exclude(mostrar_precio=False).update(mostrar_precio=False)
        self.message_user(
            request,
            f'Se desactivó el precio en {actualizados} producto(s). '
            'El precio capturado se conserva.',
            messages.SUCCESS,
        )

    # --- Columnas ---------------------------------------------------------

    @admin.display(description='Precio', ordering='precio')
    def precio_en_lista(self, obj):
        if obj.precio is None:
            return '—'
        if obj.mostrar_precio:
            return obj.precio_formateado
        return format_html(
            '<span style="text-decoration:line-through;opacity:0.6;" '
            'title="Precio guardado pero oculto en el sitio">{}</span>',
            obj.precio_formateado,
        )

    @admin.display(description='Editar')
    def boton_editar(self, obj):
        url = reverse('admin:tienda_producto_change', args=[obj.pk])
        return format_html(
            '<a href="{}" title="Editar {}" '
            'style="display:inline-flex;align-items:center;gap:0.3rem;white-space:nowrap;'
            'border:1px solid currentColor;border-radius:9999px;padding:0.2rem 0.75rem;'
            'font-size:0.75rem;font-weight:500;text-decoration:none;">'
            '<span class="material-symbols-outlined" style="font-size:1rem;">edit</span>Editar</a>',
            url,
            obj.nombre,
        )

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
