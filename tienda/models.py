from django.db import models
from django.utils.text import slugify


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    descripcion = models.TextField(blank=True)
    icono = models.CharField(max_length=10, blank=True, help_text='Emoji para la categoría')
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class SubCategoria(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='subcategorias')
    nombre = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, blank=True)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'subcategoría'
        verbose_name_plural = 'subcategorías'
        unique_together = ['categoria', 'slug']

    def __str__(self):
        return f'{self.categoria.nombre} > {self.nombre}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class Producto(models.Model):
    MATERIALES = [
        ('acero', 'Acero al Carbón'),
        ('galvanizado', 'Galvanizado'),
        ('inoxidable_304', 'Acero Inoxidable 304'),
        ('inoxidable_410', 'Acero Inoxidable 410'),
        ('bronce', 'Bronce'),
        ('nylon', 'Nylon'),
        ('plastico', 'Plástico'),
        ('hule', 'Hule'),
        ('otro', 'Otro'),
    ]

    ACABADOS = [
        ('pavonado', 'Pavonado'),
        ('galvanizado', 'Galvanizado'),
        ('tropicalizado', 'Tropicalizado'),
        ('cromado', 'Cromado'),
        ('sin_acabado', 'Sin Acabado'),
        ('fosfatado', 'Fosfatado'),
        ('niquelado', 'Niquelado'),
        ('otro', 'Otro'),
    ]

    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE, related_name='productos')
    codigo = models.CharField(max_length=30, unique=True, help_text='Código de familia del catálogo')
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    descripcion = models.TextField(blank=True)
    material = models.CharField(max_length=20, choices=MATERIALES, blank=True)
    acabado = models.CharField(max_length=20, choices=ACABADOS, blank=True)
    norma = models.CharField(max_length=50, blank=True, help_text='Ej: UNC, UNF, Milimétrico')
    grado = models.CharField(max_length=20, blank=True, help_text='Ej: G2, G5, G8, Clase 8.8')
    imagen = models.ImageField(upload_to='productos/', max_length=300, blank=True, help_text='Imagen del producto')
    destacado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['subcategoria', 'nombre']
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)
