from django import template
from django.utils.safestring import mark_safe

register = template.Library()

ICONOS = {
    # Tornillo con cabeza hexagonal, arandela y rosca detallada
    'tornillo': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="22,6 42,6 48,16 42,26 22,26 16,16" fill="none"/><line x1="28" y1="10" x2="36" y2="10"/><line x1="26" y1="14" x2="38" y2="14"/><line x1="28" y1="18" x2="36" y2="18"/><rect x="27" y="26" width="10" height="4" rx="1"/><line x1="29" y1="33" x2="35" y2="33"/><line x1="29" y1="36" x2="35" y2="36"/><line x1="29" y1="39" x2="35" y2="39"/><line x1="29" y1="42" x2="35" y2="42"/><line x1="29" y1="45" x2="35" y2="45"/><line x1="29" y1="48" x2="35" y2="48"/><line x1="29" y1="51" x2="35" y2="51"/><path d="M29 30V55L32 58L35 55V30"/></svg>',

    # Tuerca hexagonal con agujero central y detalle 3D
    'tuerca': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="32,4 54,15 54,37 32,48 10,37 10,15"/><polygon points="32,8 50,17.5 50,34.5 32,44 14,34.5 14,17.5" stroke-dasharray="0"/><circle cx="32" cy="26" r="8"/><circle cx="32" cy="26" r="5" stroke-dasharray="2 2"/><line x1="10" y1="15" x2="14" y2="17.5"/><line x1="54" y1="15" x2="50" y2="17.5"/><line x1="32" y1="48" x2="32" y2="44"/><path d="M32 4V8" /><path d="M54 15L50 17.5"/><path d="M10 15L14 17.5"/><ellipse cx="32" cy="26" rx="11" ry="3" stroke-opacity="0.3"/></svg>',

    # Rondana / arandela con perspectiva y grosor
    'rondana': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="32" cy="28" rx="22" ry="10"/><ellipse cx="32" cy="32" rx="22" ry="10"/><line x1="10" y1="28" x2="10" y2="32"/><line x1="54" y1="28" x2="54" y2="32"/><ellipse cx="32" cy="28" rx="9" ry="4"/><ellipse cx="32" cy="32" rx="9" ry="4"/><line x1="23" y1="28" x2="23" y2="32"/><line x1="41" y1="28" x2="41" y2="32"/><ellipse cx="32" cy="30" rx="16" ry="7" stroke-opacity="0.2" stroke-dasharray="3 3"/></svg>',

    # Opresor / set screw con allen y cuerpo roscado
    'opresor': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="22" y="6" width="20" height="12" rx="2"/><polygon points="28,10 36,10 34,14 30,14"/><rect x="24" y="18" width="16" height="6"/><path d="M24 24V52L28 56H36L40 52V24"/><line x1="26" y1="28" x2="38" y2="28"/><line x1="26" y1="32" x2="38" y2="32"/><line x1="26" y1="36" x2="38" y2="36"/><line x1="26" y1="40" x2="38" y2="40"/><line x1="26" y1="44" x2="38" y2="44"/><line x1="26" y1="48" x2="38" y2="48"/><circle cx="32" cy="11" r="3"/></svg>',

    # Pija / tornillo autorroscante con cabeza phillips y punta afilada
    'pija': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="32" cy="10" rx="14" ry="5"/><ellipse cx="32" cy="12" rx="14" ry="5"/><line x1="18" y1="10" x2="18" y2="12"/><line x1="46" y1="10" x2="46" y2="12"/><line x1="28" y1="8" x2="36" y2="12"/><line x1="36" y1="8" x2="28" y2="12"/><path d="M26 14V46L32 58L38 46V14"/><line x1="26" y1="20" x2="38" y2="20"/><line x1="27" y1="26" x2="37" y2="26"/><line x1="28" y1="32" x2="36" y2="32"/><line x1="29" y1="38" x2="35" y2="38"/><line x1="30" y1="44" x2="34" y2="44"/><line x1="31" y1="50" x2="33" y2="50"/></svg>',

    # Taquete de expansión con aletas y ranuras
    'taquete': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="24" y="4" width="16" height="8" rx="2"/><path d="M24 12H40V20H24Z"/><path d="M22 20H42L44 28H20L22 20Z"/><path d="M20 28H44V36H20Z"/><line x1="24" y1="32" x2="40" y2="32"/><path d="M20 36L16 52H24L22 36"/><path d="M44 36L48 52H40L42 36"/><path d="M28 36V54L32 58L36 54V36"/><line x1="28" y1="42" x2="36" y2="42"/><line x1="28" y1="48" x2="36" y2="48"/><line x1="30" y1="24" x2="34" y2="24"/></svg>',

    # Varilla roscada completa con tuercas en los extremos
    'varilla': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="27,2 37,2 39,6 37,10 27,10 25,6"/><rect x="29" y="10" width="6" height="44"/><line x1="29" y1="14" x2="35" y2="14"/><line x1="29" y1="18" x2="35" y2="18"/><line x1="29" y1="22" x2="35" y2="22"/><line x1="29" y1="26" x2="35" y2="26"/><line x1="29" y1="30" x2="35" y2="30"/><line x1="29" y1="34" x2="35" y2="34"/><line x1="29" y1="38" x2="35" y2="38"/><line x1="29" y1="42" x2="35" y2="42"/><line x1="29" y1="46" x2="35" y2="46"/><line x1="29" y1="50" x2="35" y2="50"/><polygon points="27,54 37,54 39,58 37,62 27,62 25,58"/></svg>',

    # Acero inoxidable - escudo con rayo/brillo
    'inoxidable': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M32 4L52 14V30C52 44 42 54 32 60C22 54 12 44 12 30V14L32 4Z"/><path d="M32 8L48 16V30C48 42 40 50 32 56C24 50 16 42 16 30V16L32 8Z" stroke-opacity="0.3"/><path d="M28 22L24 34H30L26 46L40 28H33L38 18Z" fill="none" stroke-width="2.5"/><line x1="44" y1="8" x2="48" y2="4" stroke-width="1.5"/><line x1="48" y1="10" x2="54" y2="8" stroke-width="1.5"/><line x1="50" y1="14" x2="56" y2="14" stroke-width="1.5"/></svg>',

    # Fijación y soportería - abrazadera/clamp con soporte
    'fijacion': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="8" y="28" width="48" height="8" rx="2"/><rect x="12" y="20" width="8" height="8" rx="1"/><rect x="44" y="20" width="8" height="8" rx="1"/><circle cx="16" cy="24" r="2"/><circle cx="48" cy="24" r="2"/><path d="M16 36V52"/><path d="M48 36V52"/><rect x="10" y="52" width="12" height="4" rx="1"/><rect x="42" y="52" width="12" height="4" rx="1"/><path d="M24 32H40" stroke-dasharray="3 2"/><line x1="28" y1="20" x2="28" y2="28"/><line x1="36" y1="20" x2="36" y2="28"/><path d="M28 16L32 12L36 16"/><line x1="32" y1="12" x2="32" y2="20"/></svg>',

    # Estructural - viga I con pernos
    'estructural': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="12" y="4" width="40" height="8" rx="1"/><rect x="12" y="52" width="40" height="8" rx="1"/><rect x="26" y="12" width="12" height="40"/><line x1="16" y1="8" x2="16" y2="4"/><line x1="48" y1="8" x2="48" y2="4"/><line x1="16" y1="52" x2="16" y2="56"/><line x1="48" y1="52" x2="48" y2="56"/><circle cx="20" cy="8" r="2" fill="currentColor"/><circle cx="44" cy="8" r="2" fill="currentColor"/><circle cx="20" cy="56" r="2" fill="currentColor"/><circle cx="44" cy="56" r="2" fill="currentColor"/><line x1="26" y1="22" x2="38" y2="22" stroke-opacity="0.4"/><line x1="26" y1="32" x2="38" y2="32" stroke-opacity="0.4"/><line x1="26" y1="42" x2="38" y2="42" stroke-opacity="0.4"/></svg>',

    # Automotriz - engranaje/gear detallado
    'automotriz': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M28 4H36V10L40 12L44 8L50 14L46 18L48 22H54V30H48L46 34L50 38L44 44L40 40L36 42V48H28V42L24 40L20 44L14 38L18 34L16 30H10V22H16L18 18L14 14L20 8L24 12L28 10V4Z"/><circle cx="32" cy="26" r="8"/><circle cx="32" cy="26" r="4"/><circle cx="32" cy="26" r="1.5" fill="currentColor"/><path d="M32 52V58" stroke-width="3"/><circle cx="26" cy="58" r="4"/><circle cx="38" cy="58" r="4"/><circle cx="26" cy="58" r="1.5" fill="currentColor"/><circle cx="38" cy="58" r="1.5" fill="currentColor"/><line x1="22" y1="58" x2="10" y2="58"/><line x1="42" y1="58" x2="54" y2="58"/></svg>',

    # Ferretería general - caja de herramientas abierta con herramientas
    'ferreteria': '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="6" y="28" width="52" height="28" rx="3"/><path d="M20 28V20H44V28"/><rect x="28" y="16" width="8" height="4" rx="1"/><line x1="6" y1="40" x2="58" y2="40"/><rect x="24" y="34" width="16" height="12" rx="1"/><circle cx="32" cy="40" r="3"/><path d="M18 28L14 12L18 8" stroke-width="2.5"/><path d="M46 28L44 14L48 10" stroke-width="2.5"/><circle cx="18" cy="8" r="2" fill="currentColor"/><path d="M48 10L50 8L52 10" stroke-width="2"/><line x1="12" y1="48" x2="18" y2="48" stroke-opacity="0.4"/><line x1="46" y1="48" x2="52" y2="48" stroke-opacity="0.4"/></svg>',
}

ICON_ALIASES = {
    'tornillos': 'tornillo',
    'tuercas': 'tuerca',
    'rondanas': 'rondana',
    'opresores': 'opresor',
    'pijas': 'pija',
    'taquetes': 'taquete',
    'varillas-roscadas': 'varilla',
    'acero-inoxidable': 'inoxidable',
    'fijacion-y-soporteria': 'fijacion',
    'estructural': 'estructural',
    'automotriz': 'automotriz',
    'ferreteria-general': 'ferreteria',
}


@register.simple_tag
def icono(nombre, size=24, color='currentColor', css_class=''):
    key = ICON_ALIASES.get(nombre, nombre)
    svg = ICONOS.get(key, ICONOS['tornillo'])
    cls = f' class="{css_class}"' if css_class else ''
    styled = svg.replace(
        '<svg ',
        f'<svg width="{size}" height="{size}" style="color:{color};flex-shrink:0;"{cls} ',
        1,
    )
    return mark_safe(styled)
