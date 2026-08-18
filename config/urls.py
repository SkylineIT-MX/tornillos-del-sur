"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.templatetags.static import static as static_url
from django.urls import include, path, re_path
from django.views.generic.base import RedirectView
from django.views.static import serve

from tienda.sitemaps import (
    StaticViewSitemap, CategoriaSitemap, SubCategoriaSitemap, ProductoSitemap,
)

sitemaps = {
    'static': StaticViewSitemap,
    'categorias': CategoriaSitemap,
    'subcategorias': SubCategoriaSitemap,
    'productos': ProductoSitemap,
}


def robots_txt(request):
    lines = [
        'User-agent: *',
        'Allow: /',
        'Disallow: /admin/',
        '',
        'Sitemap: https://tornillosdelsur.com.mx/sitemap.xml',
    ]
    return HttpResponse('\n'.join(lines), content_type='text/plain')


def google_site_verification(request):
    return HttpResponse(
        'google-site-verification: googleb2651373df8160ec.html',
        content_type='text/html',
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', robots_txt),
    # Los navegadores y algunos crawlers piden /favicon.ico en la raíz
    path(
        'favicon.ico',
        RedirectView.as_view(url=static_url('tienda/images/icons/favicon.ico'), permanent=True),
    ),
    path('googleb2651373df8160ec.html', google_site_verification),
    path('', include('tienda.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
