from django.contrib.sitemaps import Sitemap
from django.contrib.sites.requests import RequestSite
from django.urls import reverse

from .models import Categoria, SubCategoria, Producto


class _BaseSitemap(Sitemap):
    """Sitemap base que fuerza el dominio canónico, ignorando la tabla Sites."""
    protocol = 'https'

    def get_urls(self, page=1, site=None, protocol=None):
        site = _CanonicalSite()
        return super().get_urls(page=page, site=site, protocol=protocol)


class _CanonicalSite:
    domain = 'tornillosdelsur.com.mx'
    name = 'Tornillos del Sur'


class StaticViewSitemap(_BaseSitemap):
    priority = 0.9
    changefreq = 'weekly'

    def items(self):
        return ['tienda:index', 'tienda:catalogo', 'tienda:seguridad_industrial']

    def location(self, item):
        return reverse(item)


class CategoriaSitemap(_BaseSitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return Categoria.objects.all()

    def location(self, obj):
        return reverse('tienda:categoria', args=[obj.slug])


class SubCategoriaSitemap(_BaseSitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return SubCategoria.objects.all()

    def location(self, obj):
        return reverse('tienda:subcategoria', args=[obj.categoria.slug, obj.slug])


class ProductoSitemap(_BaseSitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        return Producto.objects.filter(activo=True)

    def lastmod(self, obj):
        return obj.creado

    def location(self, obj):
        return reverse('tienda:producto', args=[obj.codigo])
