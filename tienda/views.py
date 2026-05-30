from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

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


def buscar(request):
    query = (request.GET.get('q') or '').strip()
    productos = Producto.objects.none()
    if query:
        terms = [t for t in query.split() if t]
        condicion = Q()
        for term in terms:
            condicion &= (
                Q(nombre__icontains=term)
                | Q(codigo__icontains=term)
                | Q(descripcion__icontains=term)
                | Q(subcategoria__nombre__icontains=term)
                | Q(subcategoria__categoria__nombre__icontains=term)
                | Q(norma__icontains=term)
                | Q(grado__icontains=term)
            )
        productos = (
            Producto.objects.filter(condicion, activo=True)
            .select_related('subcategoria__categoria')
            .distinct()
        )
    return render(request, 'tienda/buscar.html', {
        'query': query,
        'productos': productos,
        'total': productos.count() if query else 0,
        'categorias': Categoria.objects.all(),
    })


def buscar_sugerencias(request):
    query = (request.GET.get('q') or '').strip()
    results = []
    if len(query) >= 2:
        terms = [t for t in query.split() if t]
        condicion = Q()
        for term in terms:
            condicion &= (
                Q(nombre__icontains=term)
                | Q(codigo__icontains=term)
                | Q(subcategoria__nombre__icontains=term)
                | Q(subcategoria__categoria__nombre__icontains=term)
            )
        qs = (
            Producto.objects.filter(condicion, activo=True)
            .select_related('subcategoria__categoria')
            .distinct()[:7]
        )
        for p in qs:
            results.append({
                'codigo': p.codigo,
                'nombre': p.nombre,
                'categoria': p.subcategoria.categoria.nombre,
                'subcategoria': p.subcategoria.nombre,
                'imagen': f'/media/{p.imagen}' if p.imagen else '',
                'url': reverse('tienda:producto', args=[p.codigo]),
            })
    return JsonResponse({'query': query, 'results': results})
