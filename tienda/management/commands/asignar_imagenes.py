"""Asocia los archivos de media/ a cada Producto buscando coincidencias por nombre.

El nombre del archivo se construye reemplazando '/' por '_' en producto.nombre
y añadiendo una de las extensiones soportadas (.png, .jpg, .jpeg, .tiff, .webp).
La búsqueda recorre todas las subcarpetas de MEDIA_ROOT, por lo que la categoría
de la carpeta no necesita coincidir con la del producto en la base de datos.
"""
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from tienda.models import Producto


EXTENSIONES = ('.png', '.jpg', '.jpeg', '.tiff', '.tif', '.webp')


def nombre_archivo_base(producto_nombre: str) -> str:
    return producto_nombre.replace('/', '_').strip()


class Command(BaseCommand):
    help = 'Asocia imágenes en MEDIA_ROOT a cada Producto por coincidencia de nombre.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--dry-run',
            action='store_true',
            help='Muestra las coincidencias sin guardar cambios.',
        )
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Limpia el campo imagen antes de re-escanear.',
        )

    def handle(self, *args, **options):
        media_root = Path(settings.MEDIA_ROOT)
        if not media_root.exists():
            self.stderr.write(self.style.ERROR(f'MEDIA_ROOT no existe: {media_root}'))
            return

        # Index: nombre base (sin extensión, case-insensitive) -> Path relativo
        indice = {}
        for archivo in media_root.rglob('*'):
            if not archivo.is_file():
                continue
            if archivo.suffix.lower() not in EXTENSIONES:
                continue
            clave = archivo.stem.lower()
            # Preferimos .png > .jpg > .jpeg > .webp > .tiff
            actual = indice.get(clave)
            if actual is None or self._prioridad(archivo.suffix) < self._prioridad(actual.suffix):
                indice[clave] = archivo

        if options['reset']:
            Producto.objects.exclude(imagen='').update(imagen='')
            self.stdout.write(self.style.WARNING('Campo imagen limpiado para todos los productos.'))

        asignados = 0
        sin_imagen = []
        for producto in Producto.objects.all():
            base = nombre_archivo_base(producto.nombre).lower()
            archivo = indice.get(base)
            if archivo is None:
                sin_imagen.append(producto.nombre)
                continue

            ruta_relativa = archivo.relative_to(media_root).as_posix()
            if producto.imagen != ruta_relativa:
                if not options['dry_run']:
                    producto.imagen = ruta_relativa
                    producto.save(update_fields=['imagen'])
                asignados += 1
                self.stdout.write(f'  ✓ {producto.nombre}  ->  {ruta_relativa}')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(
            f'{asignados} productos asignados. {len(sin_imagen)} sin imagen.'
        ))
        if sin_imagen and options.get('verbosity', 1) >= 2:
            self.stdout.write('')
            self.stdout.write('Productos sin imagen:')
            for nombre in sin_imagen:
                self.stdout.write(f'  - {nombre}')

    @staticmethod
    def _prioridad(extension: str) -> int:
        orden = {'.png': 0, '.webp': 1, '.jpg': 2, '.jpeg': 2, '.tiff': 3, '.tif': 3}
        return orden.get(extension.lower(), 9)
