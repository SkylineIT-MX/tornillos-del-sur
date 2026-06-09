from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Categoria, SubCategoria, Producto


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return ['tienda:index', 'tienda:catalogo', 'tienda:seguridad_industrial']

    def location(self, item):
        return reverse(item)


class CategoriaSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return Categoria.objects.all()

    def location(self, obj):
        return reverse('tienda:categoria', args=[obj.slug])


class SubCategoriaSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        return SubCategoria.objects.all()

    def location(self, obj):
        return reverse('tienda:subcategoria', args=[obj.categoria.slug, obj.slug])


class ProductoSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return Producto.objects.filter(activo=True)

    def lastmod(self, obj):
        return obj.creado

    def location(self, obj):
        return reverse('tienda:producto', args=[obj.codigo])
