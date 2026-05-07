from django.shortcuts import render, get_object_or_404

from .models import Categoria, SubCategoria, Producto


def index(request):
    categorias = Categoria.objects.prefetch_related('subcategorias').all()
    destacados = Producto.objects.filter(destacado=True).select_related('subcategoria__categoria')[:8]
    return render(request, 'tienda/index.html', {
        'categorias': categorias,
        'destacados': destacados,
    })


def categoria_detalle(request, slug):
    categoria = get_object_or_404(Categoria.objects.prefetch_related('subcategorias__productos'), slug=slug)
    productos = Producto.objects.filter(subcategoria__categoria=categoria).select_related('subcategoria')
    return render(request, 'tienda/categoria.html', {
        'categoria': categoria,
        'productos': productos,
        'categorias': Categoria.objects.all(),
    })


def subcategoria_detalle(request, cat_slug, sub_slug):
    categoria = get_object_or_404(Categoria, slug=cat_slug)
    subcategoria = get_object_or_404(SubCategoria, slug=sub_slug, categoria=categoria)
    productos = subcategoria.productos.all()
    return render(request, 'tienda/subcategoria.html', {
        'categoria': categoria,
        'subcategoria': subcategoria,
        'productos': productos,
        'categorias': Categoria.objects.all(),
    })


def producto_detalle(request, codigo):
    producto = get_object_or_404(
        Producto.objects.select_related('subcategoria__categoria'),
        codigo=codigo,
    )
    relacionados = Producto.objects.filter(
        subcategoria=producto.subcategoria,
    ).exclude(pk=producto.pk)[:4]
    return render(request, 'tienda/producto.html', {
        'producto': producto,
        'relacionados': relacionados,
        'categorias': Categoria.objects.all(),
    })


def catalogo(request):
    categorias = Categoria.objects.prefetch_related('subcategorias__productos').all()
    total_productos = Producto.objects.count()
    return render(request, 'tienda/catalogo.html', {
        'categorias': categorias,
        'total_productos': total_productos,
    })


def seguridad_industrial(request):
    return render(request, 'tienda/seguridad_industrial.html', {
        'categorias': Categoria.objects.all(),
    })
