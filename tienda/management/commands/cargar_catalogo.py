from django.core.management.base import BaseCommand
from tienda.models import Categoria, SubCategoria, Producto


CATALOGO = {
    # =====================================================================
    # 1. TORNILLOS
    # =====================================================================
    'Tornillos': {
        'icono': 'tornillo',
        'descripcion': 'Amplia variedad de tornillos para uso industrial, estructural y doméstico en diferentes materiales, grados y acabados.',
        'orden': 1,
        'subcategorias': {
            'Tornillos Hexagonales': {
                'descripcion': 'Tornillos con cabeza hexagonal para uso general e industrial. Disponibles en grados 2, 5 y 8.',
                'productos': [
                    {'codigo': 'MAG', 'nombre': 'Tornillo Hexagonal Máquina UNC Estándar G/2', 'descripcion': 'Tornillo hexagonal tipo máquina con rosca UNC estándar grado 2. Uso general en ensambles que no requieren alta resistencia. Ideal para uniones en estructuras ligeras y maquinaria.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'MG', 'nombre': 'Tornillo Hexagonal UNC Estándar G/5', 'descripcion': 'Tornillo hexagonal con rosca UNC grado 5. Mayor resistencia a la tracción, ideal para aplicaciones automotrices e industriales que requieren mayor torque de apriete.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'GSSGALV', 'nombre': 'Tornillo Hexagonal UNC Estándar G/5 Galvanizado', 'descripcion': 'Tornillo hexagonal grado 5 con acabado galvanizado por inmersión en caliente. Resistente a la corrosión para uso en exteriores y ambientes húmedos.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'GSF', 'nombre': 'Tornillo Hexagonal UNF Fino G/5', 'descripcion': 'Tornillo hexagonal con rosca UNF (fina) grado 5. La rosca fina proporciona mayor resistencia al aflojamiento y mejor ajuste en aplicaciones de precisión.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNF', 'grado': 'G5'},
                    {'codigo': 'G8S', 'nombre': 'Tornillo Hexagonal UNC Estándar G/8', 'descripcion': 'Tornillo hexagonal grado 8, la máxima resistencia en tornillería estándar. Para aplicaciones críticas en maquinaria pesada, equipos agrícolas y estructuras de alta exigencia.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G8'},
                    {'codigo': 'G8F', 'nombre': 'Tornillo Hexagonal UNF Fino G/8', 'descripcion': 'Tornillo hexagonal con rosca fina UNF grado 8. Combina la máxima resistencia del grado 8 con la precisión de la rosca fina.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNF', 'grado': 'G8'},
                    {'codigo': 'GSSTROP', 'nombre': 'Tornillo Hexagonal UNC Estándar Tropicalizado', 'descripcion': 'Tornillo hexagonal con acabado tropicalizado (zinc amarillo). Ofrece buena resistencia a la corrosión con apariencia dorada.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'HMMS', 'nombre': 'Tornillo Hexagonal Milimétrico Clase 8.8', 'descripcion': 'Tornillo hexagonal con rosca métrica clase 8.8. Equivalente al grado 5 SAE. Amplio uso en maquinaria europea e industria automotriz.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 8.8'},
                    {'codigo': 'HMS', 'nombre': 'Tornillo Hexagonal Milimétrico Clase 10.9', 'descripcion': 'Tornillo hexagonal métrico clase 10.9 de alta resistencia. Para aplicaciones industriales críticas donde se requiere máximo torque.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 10.9'},
                    {'codigo': 'EA325', 'nombre': 'Tornillo Hexagonal Estructural A325', 'descripcion': 'Tornillo estructural de alta resistencia norma ASTM A325. Diseñado para conexiones estructurales de acero en edificaciones, puentes y naves industriales.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'A325', 'destacado': True},
                    {'codigo': 'CNEG', 'nombre': 'Tornillo Hexagonal Cuerda Corrida UNC Estándar G/2 Sin Acabado', 'descripcion': 'Tornillo hexagonal con cuerda corrida (rosca completa) sin acabado. La cuerda completa proporciona mayor área de agarre y versatilidad de corte.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'COCHEGALV', 'nombre': 'Tornillo de Coche UNC Estándar G/2 Galvanizado', 'descripcion': 'Tornillo de coche (cabeza redonda con cuello cuadrado) galvanizado. Ideal para uniones en madera y metal donde se requiere que la cabeza quede lisa.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'ACMM', 'nombre': 'Tornillo Cabeza de Coche UNC Estándar G/5', 'descripcion': 'Tornillo de coche grado 5 pavonado. Cabeza semiesférica con cuello cuadrado que evita el giro durante el apriete.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'AGBMM', 'nombre': 'Tornillo Hexagonal Cuerda Corrida UNC Estándar G/5 Galvanizado', 'descripcion': 'Tornillo hexagonal grado 5 con cuerda corrida y acabado galvanizado. Combina alta resistencia con protección anticorrosiva.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G5'},
                ],
            },
            'Tornillos Allen': {
                'descripcion': 'Tornillos con cabeza cilíndrica y hueco hexagonal interior (Allen). Para espacios reducidos y montajes de precisión.',
                'productos': [
                    {'codigo': 'ABS', 'nombre': 'Tornillo Allen Cabeza Botón UNC Estándar', 'descripcion': 'Tornillo Allen con cabeza tipo botón (semiesférica) y rosca UNC. Acabado estético para superficies visibles en maquinaria y equipos.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'Clase 10.9'},
                    {'codigo': 'APMM', 'nombre': 'Tornillo Allen Cabeza Plana UNC Estándar', 'descripcion': 'Tornillo Allen con cabeza avellanada (plana) para montaje al ras. Ideal cuando se necesita una superficie completamente lisa.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'Clase 10.9'},
                    {'codigo': 'APS', 'nombre': 'Tornillo Allen Cabeza Plana Milimétrico', 'descripcion': 'Tornillo Allen avellanado con rosca métrica. Para aplicaciones de ingeniería de precisión y equipos importados con sistema métrico.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 10.9'},
                    {'codigo': 'ACMMS', 'nombre': 'Tornillo Allen Cilíndrico Cabeza Milimétrico Clase 12.9', 'descripcion': 'Tornillo Allen cilíndrico clase 12.9 con rosca métrica. La clase más alta de resistencia disponible en tornillos Allen estándar.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 12.9', 'destacado': True},
                    {'codigo': 'CSMUELLE', 'nombre': 'Tornillo Allen Guía Milimétrico Clase 12.9', 'descripcion': 'Tornillo Allen tipo guía (sin cabeza, con espiga) clase 12.9. Utilizado como pasador guía en moldes, troqueles y herramientas de precisión.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 12.9'},
                    {'codigo': 'ARA5S', 'nombre': 'Tornillo Allen Cabeza Botón Milimétrico Clase 10.9 Sin Acabado', 'descripcion': 'Tornillo Allen botón métrico sin acabado superficial. Para aplicaciones internas donde no se requiere protección anticorrosiva.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': 'Milimétrico', 'grado': 'Clase 10.9'},
                ],
            },
            'Tornillos Especiales': {
                'descripcion': 'Tornillos de uso específico: arado, elevador, estufa, jaladeras y más.',
                'productos': [
                    {'codigo': 'ARATOP3', 'nombre': 'Tornillo Arado Top 3 UNC Estándar G/5', 'descripcion': 'Tornillo de arado grado 5 con cabeza avellanada y cuello cuadrado. Diseñado para implementos agrícolas como arados, rastras y cultivadores.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'ARAGB5', 'nombre': 'Tornillo Arado Top 3 UNC Estándar G/8', 'descripcion': 'Tornillo de arado grado 8. Máxima resistencia para implementos agrícolas pesados sometidos a gran esfuerzo de corte.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G8'},
                    {'codigo': 'TORXTF', 'nombre': 'Tornillo Torx Punta F UNC', 'descripcion': 'Tornillo con cabeza Torx y punta autoperforante. La cabeza Torx ofrece mayor transmisión de torque que Phillips o hexagonal.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TORXT23', 'nombre': 'Tornillo Torx Punta T-23 UNC Estándar', 'descripcion': 'Tornillo con cabeza Torx T-23 y rosca UNC. Diseño resistente al desgaste del dado, ideal para líneas de ensamble automatizadas.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'FLAV', 'nombre': 'Tornillo Flange UNC Estándar', 'descripcion': 'Tornillo hexagonal con brida (flange) integrada que actúa como rondana. Reduce piezas y tiempo de ensamble en la industria automotriz.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'ELEV', 'nombre': 'Tornillo Elevador UNC Estándar', 'descripcion': 'Tornillo especial para elevadores de grano y bandas transportadoras. Cabeza plana grande con cuello cuadrado para montaje en tolvas.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'EBGALV', 'nombre': 'Tornillo Estufa Bola Galvanizado', 'descripcion': 'Tornillo de estufa con cabeza redonda ranurada y acabado galvanizado. Ideal para equipos de cocina, estufas y aplicaciones domésticas.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'GMM', 'nombre': 'Tornillo Queso Milimétrico', 'descripcion': 'Tornillo cabeza tipo queso (cheese head) con ranura y rosca métrica. Uso común en electrónica, equipos de laboratorio y aplicaciones ligeras.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'FECOR', 'nombre': 'Tornillo Reposable Milimétrico Galvanizado', 'descripcion': 'Tornillo especial reposable con rosca milimétrica y acabado galvanizado. Para aplicaciones que requieren montaje y desmontaje frecuente.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'EBSTRUSS', 'nombre': 'Tornillo para Jaladera Cabeza Truss UNC Estándar', 'descripcion': 'Tornillo con cabeza extra plana y ancha tipo Truss para fijación de jaladeras, tiradores y accesorios decorativos en muebles y puertas.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TORAGMM', 'nombre': 'Tornillo Arado Milimétrico', 'descripcion': 'Tornillo de arado con rosca métrica para implementos agrícolas de fabricación europea y maquinaria importada.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                ],
            },
        },
    },
    # =====================================================================
    # 2. TUERCAS
    # =====================================================================
    'Tuercas': {
        'icono': 'tuerca',
        'descripcion': 'Tuercas de todas las medidas y tipos para complementar cualquier sistema de fijación.',
        'orden': 2,
        'subcategorias': {
            'Tuercas Hexagonales': {
                'descripcion': 'Tuercas hexagonales estándar en grados 2, 5 y 8. El complemento esencial de todo tornillo hexagonal.',
                'productos': [
                    {'codigo': 'TLVS', 'nombre': 'Tuerca Hexagonal UNC Estándar G/2', 'descripcion': 'Tuerca hexagonal grado 2 con rosca UNC estándar. Para uso general en uniones no críticas con tornillos grado 2.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'TLVSGC', 'nombre': 'Tuerca Hexagonal UNC Estándar GC Galvanizada', 'descripcion': 'Tuerca hexagonal galvanizada para uso en exteriores. El acabado por inmersión en caliente garantiza máxima protección anticorrosiva.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'TG5', 'nombre': 'Tuerca Hexagonal UNC Estándar G/5', 'descripcion': 'Tuerca hexagonal grado 5 pavonada. Para ensambles de media a alta resistencia en maquinaria e industria automotriz.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'TG5F', 'nombre': 'Tuerca Hexagonal UNF Fina G/5', 'descripcion': 'Tuerca hexagonal con rosca fina UNF grado 5. Mayor resistencia al aflojamiento por vibración.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNF', 'grado': 'G5'},
                    {'codigo': 'TGSSGALV', 'nombre': 'Tuerca Hexagonal UNC Estándar G/5 Galvanizada', 'descripcion': 'Tuerca grado 5 con acabado galvanizado. Combina alta resistencia mecánica con protección contra la corrosión.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'TG5STROP', 'nombre': 'Tuerca Hexagonal UNC Estándar G/5 Tropicalizada', 'descripcion': 'Tuerca grado 5 con acabado tropicalizado (zinc amarillo). Aspecto dorado con buena resistencia a la corrosión.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'T8S', 'nombre': 'Tuerca Hexagonal UNC Estándar G/8', 'descripcion': 'Tuerca hexagonal grado 8 para uso con tornillos grado 8 en aplicaciones de alta exigencia estructural y mecánica.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G8'},
                    {'codigo': 'T8SF', 'nombre': 'Tuerca Hexagonal UNF Fina G/8', 'descripcion': 'Tuerca grado 8 con rosca fina. Para las aplicaciones más exigentes donde se necesita máxima resistencia y precisión.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNF', 'grado': 'G8'},
                    {'codigo': 'T2H', 'nombre': 'Tuerca Hexagonal 2H UNC Estándar', 'descripcion': 'Tuerca pesada 2H para pernos estructurales A325 y A490. Norma ASTM A194 para conexiones estructurales de acero.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': '2H', 'destacado': True},
                    {'codigo': 'TGSAMUELLE', 'nombre': 'Tuerca Alta de Muelle G/5 UNF Pavonada', 'descripcion': 'Tuerca alta especial para resortes y muelles. Mayor altura que la tuerca estándar para mejor agarre en ejes y pasadores.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNF', 'grado': 'G5'},
                    {'codigo': 'THMMS', 'nombre': 'Tuerca Hexagonal Milimétrica Clase 8.8', 'descripcion': 'Tuerca hexagonal métrica clase 8. Compatible con tornillos milimétricos clase 8.8 y 10.9.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 8'},
                ],
            },
            'Tuercas Especiales': {
                'descripcion': 'Tuercas de seguridad, mariposa, inserción, bellota y otros tipos especiales.',
                'productos': [
                    {'codigo': 'TAIT', 'nombre': 'Tuerca Automotriz Tipo K Hexagonal de Lujo Cromada', 'descripcion': 'Tuerca cromada decorativa para rines automotrices. Acabado espejo de alta calidad para vehículos de lujo.', 'material': 'acero', 'acabado': 'cromado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TAUTOMM', 'nombre': 'Tuerca Automotriz Cromada', 'descripcion': 'Tuerca automotriz estándar con acabado cromado. Para uso en rines de aluminio y acero de vehículos ligeros.', 'material': 'acero', 'acabado': 'cromado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'TAUTCONX', 'nombre': 'Tuerca Automotriz Tipo K Cónica Cromada', 'descripcion': 'Tuerca cónica cromada que proporciona centrado perfecto del rin. Diseño cónico a 60° estándar automotriz.', 'material': 'acero', 'acabado': 'cromado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'TAUTRI', 'nombre': 'Tuerca Automotriz Nissan 7/8 Cromada', 'descripcion': 'Tuerca especializada para vehículos Nissan con asiento 7/8. Acabado cromado de alta durabilidad.', 'material': 'acero', 'acabado': 'cromado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'TBELLINGALV', 'nombre': 'Tuerca Bellota UNC Estándar Galvanizada', 'descripcion': 'Tuerca tipo bellota (ciega) que cubre completamente la rosca del tornillo. Acabado estético y protección contra lesiones por roscas expuestas.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TRESOK', 'nombre': 'Tuerca Resorte UNC Estándar', 'descripcion': 'Tuerca con resorte de retención integrado tipo Kep. Incluye rondana de presión dentada para prevenir aflojamiento por vibración.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TNV', 'nombre': 'Tuerca Insert de Nylon Milimétrica', 'descripcion': 'Tuerca de seguridad con inserto de nylon (Nyloc) que previene el aflojamiento. El anillo de nylon se deforma sobre la rosca creando fricción permanente.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': '', 'destacado': True},
                    {'codigo': 'TNVNF', 'nombre': 'Tuerca Insert de Nylon UNF Fina', 'descripcion': 'Tuerca Nyloc con rosca fina UNF. Doble seguridad contra aflojamiento: rosca fina más inserto de nylon.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNF', 'grado': ''},
                    {'codigo': 'TNVMMS', 'nombre': 'Tuerca Insert de Nylon Milimétrica Clase 4.8', 'descripcion': 'Tuerca Nyloc métrica clase 4.8 para aplicaciones de resistencia media con seguridad antivibración.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 4.8'},
                    {'codigo': 'TMARGALV', 'nombre': 'Tuerca Mariposa UNC Estándar Galvanizada', 'descripcion': 'Tuerca con alas tipo mariposa para apriete manual sin herramientas. Ideal para sujeciones temporales y ajustes frecuentes.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TMARGGALMM', 'nombre': 'Tuerca Mariposa Milimétrica Clase 4.8 Galvanizada', 'descripcion': 'Tuerca mariposa con rosca métrica y acabado galvanizado. Para ensambles rápidos en equipos con sistema métrico.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'Milimétrico', 'grado': 'Clase 4.8'},
                    {'codigo': 'TFLANCES', 'nombre': 'Tuerca Flange UNC Estándar', 'descripcion': 'Tuerca hexagonal con brida serrada integrada que actúa como rondana de presión. Elimina la necesidad de rondana adicional.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TSGPOCGS', 'nombre': 'Tuerca Grupo UNF Fina G/8', 'descripcion': 'Tuerca tipo grupo (castle nut) con ranuras para pasador de seguridad. Usada en ejes, suspensiones y direcciones automotrices.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNF', 'grado': 'G8'},
                    {'codigo': 'TACME', 'nombre': 'Tuerca ACME', 'descripcion': 'Tuerca con rosca trapezoidal ACME para husillos de movimiento lineal. Usada en prensas, tornos, gatos mecánicos y sistemas de elevación.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': 'ACME', 'grado': ''},
                ],
            },
        },
    },
    # =====================================================================
    # 3. RONDANAS
    # =====================================================================
    'Rondanas': {
        'icono': 'rondana',
        'descripcion': 'Rondanas planas y de presión para distribuir carga, proteger superficies y prevenir aflojamiento.',
        'orden': 3,
        'subcategorias': {
            'Rondanas Planas': {
                'descripcion': 'Rondanas planas que distribuyen la carga del tornillo sobre una superficie mayor, protegiendo el material base.',
                'productos': [
                    {'codigo': 'RPLA', 'nombre': 'Rondana Plana USS Estándar', 'descripcion': 'Rondana plana serie USS (United States Standard) de diámetro exterior amplio. Para uso general en ensambles con tornillos estándar.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'USS', 'grado': ''},
                    {'codigo': 'RPLM', 'nombre': 'Rondana Plana Milimétrica', 'descripcion': 'Rondana plana con diámetro interior métrico. Compatible con tornillería milimétrica DIN/ISO.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'RPR', 'nombre': 'Rondana Plana USS Estándar GC Pavonada', 'descripcion': 'Rondana plana USS con acabado pavonado de alta calidad. Superficie oscura y uniforme resistente a la oxidación leve.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'USS', 'grado': ''},
                    {'codigo': 'RPRGALV', 'nombre': 'Rondana Plana USS Estándar Galvanizada', 'descripcion': 'Rondana plana galvanizada por inmersión en caliente. Para uso en exteriores con tornillos galvanizados.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'USS', 'grado': ''},
                    {'codigo': 'RPLGIC', 'nombre': 'Rondana Plana USS GC Galvanizada por Inmersión en Caliente', 'descripcion': 'Rondana plana con galvanizado pesado por inmersión en caliente. Máxima protección para estructuras expuestas a intemperie severa.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'USS', 'grado': ''},
                    {'codigo': 'RPFK36', 'nombre': 'Rondana F436 UNC Estándar', 'descripcion': 'Rondana estructural norma ASTM F436 para uso con pernos A325 y A490 en conexiones estructurales de acero.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'F436', 'destacado': True},
                    {'codigo': 'RPKIGALV', 'nombre': 'Rondana para KDSE UNC Estándar Galvanizada', 'descripcion': 'Rondana especial para sistema de anclaje KDSE. Diámetro exterior extra grande para mejor distribución de carga en concreto.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                ],
            },
            'Rondanas de Presión': {
                'descripcion': 'Rondanas de presión (split lock washers) que previenen el aflojamiento por vibración mediante tensión elástica.',
                'productos': [
                    {'codigo': 'RE4366', 'nombre': 'Rondana de Presión UNC Estándar', 'descripcion': 'Rondana de presión (guasa) tipo helicoidal que mantiene tensión constante sobre la tuerca. Estándar para prevenir aflojamiento en cualquier aplicación.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'RE4336IC', 'nombre': 'Rondana de Presión UNC Estándar GC Pavonada', 'descripcion': 'Rondana de presión de alta calidad con acabado pavonado uniforme. Bordes afilados que muerden la superficie para máxima retención.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'RSSMM', 'nombre': 'Rondana de Presión Milimétrica', 'descripcion': 'Rondana de presión para tornillería métrica. Compatible con tuercas y tornillos DIN/ISO milimétricos.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                ],
            },
        },
    },
    # =====================================================================
    # 4. OPRESORES
    # =====================================================================
    'Opresores': {
        'icono': 'opresor',
        'descripcion': 'Tornillos sin cabeza (opresores/prisioneros) para fijación de componentes en ejes y bujes.',
        'orden': 4,
        'subcategorias': {
            'Opresores': {
                'descripcion': 'Opresores con diferentes tipos de punta para sujeción de poleas, engranajes y bujes sobre ejes.',
                'productos': [
                    {'codigo': 'OAS', 'nombre': 'Opresor Punta Copa UNC Estándar', 'descripcion': 'Opresor (tornillo prisionero) con punta cóncava tipo copa y hueco hexagonal Allen. La punta copa crea una marca de centrado para reposicionamiento preciso.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'OAMM', 'nombre': 'Opresor Punta Copa Milimétrico', 'descripcion': 'Opresor con punta copa y rosca métrica. Para fijación de componentes sobre ejes en maquinaria con sistema métrico.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'OSGSCC', 'nombre': 'Opresor Set Cabeza Cuadrada UNC Estándar G/2 Sin Acabado', 'descripcion': 'Opresor con cabeza cuadrada para apriete con llave. Diseño tradicional para aplicaciones de maquinaria pesada y equipos antiguos.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'OSGSGALV', 'nombre': 'Opresor Set Cabeza Cuadrada UNC Estándar G/8 Galvanizado', 'descripcion': 'Opresor cabeza cuadrada grado 8 galvanizado. Alta resistencia con protección anticorrosiva para aplicaciones en exteriores.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G8'},
                    {'codigo': 'O5C', 'nombre': 'Opresor Set Cabeza Milimétrica Clase 12.9', 'descripcion': 'Opresor Allen con rosca métrica clase 12.9. La máxima resistencia para fijación de componentes críticos en ejes de alta velocidad.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 12.9'},
                ],
            },
        },
    },
    # =====================================================================
    # 5. PIJAS
    # =====================================================================
    'Pijas': {
        'icono': 'pija',
        'descripcion': 'Pijas (tornillos autorroscantes) para fijación en madera, lámina y materiales blandos sin necesidad de tuerca.',
        'orden': 5,
        'subcategorias': {
            'Pijas para Lámina': {
                'descripcion': 'Pijas con punta autorroscante para fijación en lámina metálica y perfiles delgados.',
                'productos': [
                    {'codigo': 'PTELALG5G', 'nombre': 'Pija Galvanizada Cabeza Hexagonal en Juego con EPDM - Galvanizada', 'descripcion': 'Pija hexagonal galvanizada con arandela de neopreno EPDM integrada. Sella la perforación contra filtraciones de agua en techos de lámina.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': '', 'destacado': True},
                    {'codigo': 'PTELALSON', 'nombre': 'Pija Galvanizada Cabeza Hexagonal Rojo en Juego con EPDM - Galvanizada', 'descripcion': 'Pija hexagonal con cabeza pintada en rojo y arandela EPDM. Para techos de lámina roja, mantiene estética uniforme.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PTELALSGV', 'nombre': 'Pija Galvanizada Cabeza Hexagonal Verde en Juego con EPDM - Galvanizada', 'descripcion': 'Pija hexagonal con cabeza verde y sello EPDM. Ideal para láminas de color verde en naves industriales y techos residenciales.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PTELALSGN', 'nombre': 'Pija Galvanizada Cabeza Hexagonal Negro en Juego con EPDM - Galvanizada', 'descripcion': 'Pija hexagonal con cabeza negra y arandela EPDM. Para láminas oscuras y cubiertas tipo teja metálica.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PTELALSGB', 'nombre': 'Pija Galvanizada Cabeza Hexagonal Beige en Juego con EPDM - Galvanizada', 'descripcion': 'Pija hexagonal con cabeza beige y sello de neopreno. Combinación discreta para láminas claras.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'BT', 'nombre': 'Pija Galvanizada Cabeza Hexagonal en Juego con EPDM - Tropicalizada', 'descripcion': 'Pija hexagonal con acabado tropicalizado y arandela EPDM. Excelente resistencia a la corrosión con tono dorado.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': '', 'grado': ''},
                ],
            },
            'Pijas para Madera': {
                'descripcion': 'Pijas diseñadas para penetrar y sujetar en madera con rosca afilada tipo AB.',
                'productos': [
                    {'codigo': 'PPBGSGG', 'nombre': 'Pija LP Punta de Broca en Juego con EPDM - Galvanizada', 'descripcion': 'Pija con punta de broca que perfora y rosca en un solo paso. Con arandela EPDM para techos. Elimina la necesidad de prebarrenado.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PPBUAP', 'nombre': 'Pija Hexagonal Punta de Broca en Juego UNC - Tropicalizada', 'descripcion': 'Pija autoperforante hexagonal con acabado tropicalizado. Para montaje rápido en perfiles metálicos sin necesidad de barreno previo.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'CHIRHEX', 'nombre': 'Chifaldo Cabeza Hexagonal', 'descripcion': 'Pija tipo chifaldo con cabeza hexagonal para fijaciones pesadas en madera. Rosca profunda de alto poder de agarre.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'CHIRPHA', 'nombre': 'Chifaldo Cabeza Phillips', 'descripcion': 'Pija chifaldo con cabeza Phillips (cruciforme) para fijación en madera. Fácil de instalar con desarmador o taladro.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                ],
            },
            'Pijas Cabeza Phillips': {
                'descripcion': 'Pijas con cabeza cruciforme Phillips para uso general en madera, plástico y lámina delgada.',
                'productos': [
                    {'codigo': 'PVNA', 'nombre': 'Pija para Concreto Cabeza Phillips AB', 'descripcion': 'Pija autorroscante para fijación directa en concreto y mampostería. Elimina la necesidad de taquete en materiales de media densidad.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PCHCONC', 'nombre': 'Pija para Concreto Cabeza Phillips AB Cuerda Estándar', 'descripcion': 'Pija para concreto con rosca estándar y cabeza Phillips. Para anclaje de marcos, canceles y elementos en muros de block.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PWC', 'nombre': 'Pija Cabeza Plana Phillips AB - Galvanizada', 'descripcion': 'Pija avellanada Phillips para montaje al ras en superficies visibles. El acabado galvanizado protege contra la humedad.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                ],
            },
            'Pijas Especiales': {
                'descripcion': 'Pijas de uso específico: K-LATH, fibroemento, multiusos y más.',
                'productos': [
                    {'codigo': 'PIABLERPBR', 'nombre': 'Pija para Tablero K-LATH Punta de Bronce', 'descripcion': 'Pija especializada para panel K-LATH (tablero de yeso con malla). Punta de bronce autoroscante para instalación rápida en construcción ligera.', 'material': 'acero', 'acabado': 'fosfatado', 'norma': '', 'grado': ''},
                    {'codigo': 'PFBCM', 'nombre': 'Pija Fibroemento Punta de Bronce', 'descripcion': 'Pija para láminas de fibrocemento con punta de bronce especial. Evita el agrietamiento del material durante la instalación.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PYCONB', 'nombre': 'Pija Multiusos Cabeza Combo Phillips-Plano', 'descripcion': 'Pija versátil con cabeza combo que acepta desarmador Phillips o plano. Para aplicaciones generales en madera, plástico y lámina.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'PPSINF', 'nombre': 'Pija para Madera Punta de Bronce 8 Cuerda Estándar', 'descripcion': 'Pija para madera con rosca completa y punta de bronce autorroscante. Para carpintería general, muebles y bastidores.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'EMPNEP', 'nombre': 'Empaque de Neopreno - Galvanizado', 'descripcion': 'Arandela de neopreno EPDM de repuesto para pijas de lámina. Sella perforaciones contra agua y humedad en techos metálicos.', 'material': 'hule', 'acabado': 'otro', 'norma': '', 'grado': ''},
                ],
            },
        },
    },
    # =====================================================================
    # 6. TAQUETES
    # =====================================================================
    'Taquetes': {
        'icono': 'taquete',
        'descripcion': 'Taquetes y anclajes para fijación en concreto, block, tabique, tablaroca y materiales huecos.',
        'orden': 6,
        'subcategorias': {
            'Taquetes de Expansión': {
                'descripcion': 'Taquetes metálicos que se expanden dentro del material base para crear anclajes de alta resistencia.',
                'productos': [
                    {'codigo': 'TAQEXPZ', 'nombre': 'Taquete Expansivo Z - Tropicalizado', 'descripcion': 'Taquete de expansión tipo Z con acabado tropicalizado. Se expande al apretar el tornillo, creando un anclaje firme en concreto y mampostería sólida.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': '', 'grado': '', 'destacado': True},
                    {'codigo': 'TAQGUNA', 'nombre': 'Taquete Expansivo Ancla - Tropicalizado', 'descripcion': 'Taquete tipo ancla de expansión para cargas pesadas en concreto. Diseño de cuña que proporciona máxima resistencia a la extracción.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': '', 'grado': ''},
                    {'codigo': 'TAQGANCHO', 'nombre': 'Taquete de Gancho / Drop', 'descripcion': 'Taquete con gancho integrado tipo drop-in para colgar objetos pesados del techo. Ideal para instalaciones eléctricas, ductos y tuberías.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                ],
            },
            'Taquetes de Plástico y Nylon': {
                'descripcion': 'Taquetes de plástico y nylon para uso general en muros, tablaroca y materiales ligeros.',
                'productos': [
                    {'codigo': 'TAQPLAS', 'nombre': 'Taquete de Plástico - Colores', 'descripcion': 'Taquete de plástico estándar disponible en varios calibres identificados por color. El más utilizado para colgar cuadros, repisas y accesorios en muros.', 'material': 'plastico', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'TAQNYLON', 'nombre': 'Taquete Nylon Cola de Pescado', 'descripcion': 'Taquete de nylon con diseño cola de pescado que se abre en forma de aleta dentro del material hueco. Ideal para tablaroca y block hueco.', 'material': 'nylon', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'TAQMEZ', 'nombre': 'Taquete Metálico para Pared', 'descripcion': 'Taquete metálico de expansión para uso en muros sólidos de concreto y tabique. Mayor resistencia que los taquetes de plástico.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                ],
            },
            'Taquetes Especiales': {
                'descripcion': 'Taquetes para aplicaciones específicas: sanitarios, mariposa, doble pared.',
                'productos': [
                    {'codigo': 'TAQMASGRIP', 'nombre': 'Sujetador/Taquete Mariposa con Tornillo - Galvanizado', 'descripcion': 'Taquete mariposa (toggler) con tornillo incluido. Se abre detrás de la superficie hueca creando un anclaje mecánico para cargas medias en tablaroca.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'TAQMASOLP', 'nombre': 'Taquete/Taquete Mariposa sin Tornillo', 'descripcion': 'Taquete mariposa vendido sin tornillo para usar con diferentes largos y calibres. Versatilidad en la selección del tornillo según la aplicación.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'TAQVTTROJ', 'nombre': 'Taquete TX Tropicalizado', 'descripcion': 'Taquete tipo TX con acabado tropicalizado para uso en concreto y tabique rojo. Diseño de aletas que maximizan el agarre.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': '', 'grado': ''},
                    {'codigo': 'JGPWC', 'nombre': 'Juego Pija para Doble Pared - Tropicalizada', 'descripcion': 'Kit completo de pija con taquete para doble muro (tablaroca + block). Incluye pija autorroscante y taquete de expansión.', 'material': 'acero', 'acabado': 'tropicalizado', 'norma': '', 'grado': ''},
                    {'codigo': 'JSGRPWC', 'nombre': 'Juego Sanitario con Tuerza Bellota y Rondana Rectangular', 'descripcion': 'Kit de fijación para WC con taquete, tornillo, tuerca bellota cromada y rondana rectangular. Todo lo necesario para instalar sanitarios.', 'material': 'acero', 'acabado': 'cromado', 'norma': '', 'grado': ''},
                ],
            },
        },
    },
    # =====================================================================
    # 7. VARILLAS ROSCADAS
    # =====================================================================
    'Varillas Roscadas': {
        'icono': 'varilla',
        'descripcion': 'Varillas roscadas (espárragos) para tensores, anclajes, colgantes y aplicaciones de sujeción continua.',
        'orden': 7,
        'subcategorias': {
            'Varillas Roscadas': {
                'descripcion': 'Varillas con rosca completa en diferentes medidas, materiales y longitudes.',
                'productos': [
                    {'codigo': 'VACME', 'nombre': 'Varilla Roscada ACME - 1 Metro', 'descripcion': 'Varilla con rosca trapezoidal ACME de 1 metro de largo. Para husillos de avance en tornos, prensas y sistemas de movimiento lineal.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': 'ACME', 'grado': ''},
                    {'codigo': 'VB712P', 'nombre': 'Varilla Roscada B7 UNC - 12 Pies (3.65 m)', 'descripcion': 'Varilla roscada grado B7 de alta resistencia, 12 pies de largo. Para pernos de espárrago en bridas de tuberías de alta presión y temperatura.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': 'UNC', 'grado': 'B7', 'destacado': True},
                    {'codigo': 'VB7', 'nombre': 'Varilla Roscada B7 UNC Estándar - 1 Metro', 'descripcion': 'Varilla roscada B7 de 1 metro. Acero aleado tratado térmicamente para aplicaciones de alta presión en refinación y petroquímica.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': 'UNC', 'grado': 'B7'},
                    {'codigo': 'VNM', 'nombre': 'Varilla Roscada Milimétrica Clase 8.8 - 1 Metro', 'descripcion': 'Varilla roscada con rosca métrica clase 8.8 de 1 metro. Para aplicaciones estructurales con sistema métrico.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': 'Clase 8.8'},
                    {'codigo': 'VG5GALV', 'nombre': 'Varilla Roscada UNC Estándar G/5 - 1 Metro Galvanizada', 'descripcion': 'Varilla roscada galvanizada grado 5 de 1 metro. Para colgantes de ductos, tuberías y bandejas de cables en exteriores.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G5'},
                    {'codigo': 'VG5', 'nombre': 'Varilla Roscada UNC Estándar G/2 - 1 Metro', 'descripcion': 'Varilla roscada grado 2 de uso general, 1 metro de largo. La opción más económica para tensores, colgantes y tirantes ligeros.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'V3MTR', 'nombre': 'Varilla Roscada UNC Estándar - 3 Metros', 'descripcion': 'Varilla roscada de 3 metros de largo. Ideal para instalaciones que requieren longitudes continuas como colgantes de plafón y ductos.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'G2'},
                    {'codigo': 'VRGALV', 'nombre': 'Varilla Roscada UNC - Galvanizada 1 Metro', 'descripcion': 'Varilla roscada galvanizada de 1 metro para uso en exteriores. Protección anticorrosiva para instalaciones expuestas.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': 'G2'},
                ],
            },
        },
    },
    # =====================================================================
    # 8. ACERO INOXIDABLE
    # =====================================================================
    'Acero Inoxidable': {
        'icono': 'inoxidable',
        'descripcion': 'Tornillería en acero inoxidable 304, 410 y 667 para ambientes corrosivos, industria alimentaria y aplicaciones marinas.',
        'orden': 8,
        'subcategorias': {
            'Tornillos Inoxidables': {
                'descripcion': 'Tornillos en acero inoxidable 304 y 410 resistentes a la corrosión.',
                'productos': [
                    {'codigo': 'ACSINOX', 'nombre': 'Tornillo Allen Cilíndrico UNC Estándar - Acero Inoxidable 304', 'descripcion': 'Tornillo Allen cilíndrico en acero inoxidable 304 (18-8). Resistente a corrosión en ambientes marinos, químicos y alimentarios.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'UNC', 'grado': '', 'destacado': True},
                    {'codigo': 'APMINOX', 'nombre': 'Tornillo Allen Cabeza Plana Milimétrico - Acero Inoxidable 304', 'descripcion': 'Tornillo Allen avellanado inoxidable 304 con rosca métrica. Montaje al ras en equipos de acero inoxidable.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'ABMINOX', 'nombre': 'Tornillo Allen Cabeza Botón Milimétrico - Acero Inoxidable 304', 'descripcion': 'Tornillo Allen botón en inoxidable 304. Cabeza decorativa semiesférica para maquinaria alimentaria y farmacéutica.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'ABWMINOX', 'nombre': 'Tornillo Allen Cabeza Botón UNC Estándar - Acero Inoxidable 304', 'descripcion': 'Tornillo Allen botón UNC en inoxidable 304. Para montajes visibles que requieren estética y resistencia a la corrosión.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'EBINOX', 'nombre': 'Tornillo Estufa Bola UNC Estándar - Acero Inoxidable 304', 'descripcion': 'Tornillo de estufa en acero inoxidable 304. Para equipos de cocina comercial, procesamiento de alimentos y ambientes húmedos.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TOSHSINOX', 'nombre': 'Tornillo Cabeza Plana Phillips UNC Estándar - Acero Inoxidable 304', 'descripcion': 'Tornillo Phillips avellanado en inoxidable 304. Para montajes al ras en superficies que requieren resistencia a la corrosión.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'DASINOX', 'nombre': 'Tornillo Cabeza Plana Phillips Milimétrico - Acero Inoxidable 304', 'descripcion': 'Tornillo Phillips plano inoxidable 304 con rosca métrica. Para aplicaciones sanitarias, decorativas y de industria alimentaria.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'HNOXX', 'nombre': 'Tornillo Hexagonal UNC Estándar - Acero Inoxidable 304', 'descripcion': 'Tornillo hexagonal en acero inoxidable 304. El más versátil para estructuras, equipos y mobiliario en ambientes corrosivos.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'HEXMXMS.V', 'nombre': 'Tornillo Hexagonal Milimétrico - Acero Inoxidable 304', 'descripcion': 'Tornillo hexagonal inoxidable 304 con rosca métrica. Para maquinaria industrial en plantas de alimentos y laboratorios.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'CNOXX', 'nombre': 'Tornillo de Coche UNC Estándar - Acero Inoxidable 304', 'descripcion': 'Tornillo de coche en inoxidable 304. Cabeza redonda con cuello cuadrado, ideal para mobiliario urbano y arquitectura.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'AINOX', 'nombre': 'Tornillo Allen Cilíndrico Milimétrico - Acero Inoxidable 304', 'descripcion': 'Tornillo Allen cilíndrico inoxidable con rosca métrica. Para equipos de procesamiento y maquinaria farmacéutica.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'Milimétrico', 'grado': ''},
                ],
            },
            'Tuercas y Rondanas Inoxidables': {
                'descripcion': 'Tuercas y rondanas en acero inoxidable para complementar tornillería anticorrosiva.',
                'productos': [
                    {'codigo': 'RPRINOX', 'nombre': 'Rondana Plana USS - Acero Inoxidable 304', 'descripcion': 'Rondana plana inoxidable 304 serie USS. Distribuye la carga y protege superficies en ambientes corrosivos.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'USS', 'grado': ''},
                    {'codigo': 'RPFBSINOX', 'nombre': 'Rondana de Presión - Acero Inoxidable 304', 'descripcion': 'Rondana de presión (guasa) en acero inoxidable 304. Seguridad antivibración con resistencia total a la corrosión.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'PPABPRINOX', 'nombre': 'Pija Phillips Punta de Bronce AB - Acero Inoxidable 304', 'descripcion': 'Pija autorroscante Phillips en inoxidable 304. Para fijación en lámina y perfiles inoxidables sin necesidad de tuerca.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'PPSINOX', 'nombre': 'Pija Hexagonal Punta de Bronce - Acero Inoxidable 410', 'descripcion': 'Pija hexagonal en acero inoxidable 410. Mayor dureza que el 304, permite perforar láminas más gruesas.', 'material': 'inoxidable_410', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'PHLAMINOX', 'nombre': 'Pija Hexagonal Punta de Bronce AB - Acero Inoxidable 410', 'descripcion': 'Pija AB hexagonal en inoxidable 410 para lámina gruesa. La punta autorroscante penetra sin prebarrenado.', 'material': 'inoxidable_410', 'acabado': 'otro', 'norma': '', 'grado': ''},
                ],
            },
            'Varillas Inoxidables': {
                'descripcion': 'Varillas roscadas en acero inoxidable para aplicaciones que exigen resistencia a la corrosión.',
                'productos': [
                    {'codigo': 'ABPSINOX', 'nombre': 'Varilla Roscada UNC Estándar - Acero Inoxidable 304 - 1 Metro', 'descripcion': 'Varilla roscada inoxidable 304 de 1 metro. Para colgantes y tensores en industria alimentaria, plantas químicas y ambientes marinos.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'VPRNOX', 'nombre': 'Varilla Roscada Milimétrica EPDM - Acero Inoxidable 304 - 1 Metro', 'descripcion': 'Varilla roscada inoxidable 304 con rosca métrica, 1 metro. Para instalaciones sanitarias y de procesamiento.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': 'Milimétrico', 'grado': ''},
                ],
            },
        },
    },
    # =====================================================================
    # 9. FIJACIÓN Y SOPORTERÍA
    # =====================================================================
    'Fijación y Soportería': {
        'icono': 'fijacion',
        'descripcion': 'Abrazaderas, mordazas, ángulos y elementos de soportería para instalaciones hidráulicas, eléctricas e industriales.',
        'orden': 9,
        'subcategorias': {
            'Abrazaderas': {
                'descripcion': 'Abrazaderas de diferentes tipos para sujeción de tubería, mangueras y conductos.',
                'productos': [
                    {'codigo': 'ABRSFINOX', 'nombre': 'Abrazadera Sinfín - Acero Inoxidable 304', 'descripcion': 'Abrazadera tipo sinfín en acero inoxidable 304. Ajuste continuo mediante tornillo sin fin para mangueras y tubería flexible en ambientes corrosivos.', 'material': 'inoxidable_304', 'acabado': 'otro', 'norma': '', 'grado': '', 'destacado': True},
                    {'codigo': 'ABROM', 'nombre': 'Abrazadera Tipo Omega - Galvanizada', 'descripcion': 'Abrazadera tipo omega para sujeción de tubería conduit y tubo galvanizado a superficies. Fijación con un solo tornillo.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'ABRPPERA', 'nombre': 'Abrazadera Tipo Pera - Galvanizada', 'descripcion': 'Abrazadera tipo pera para tubería, permite cierto movimiento térmico. Ideal para instalaciones de agua caliente y vapor.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'ABRUNA', 'nombre': 'Abrazadera Tipo Uña - Galvanizada', 'descripcion': 'Abrazadera de uña para fijación rápida de tubería en unicanal. Se engancha sin necesidad de tornillos.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'ABRUNI', 'nombre': 'Abrazadera Unicanal - Galvanizada', 'descripcion': 'Abrazadera para montaje de tubería sobre canal Unistrut/unicanal. Sistema de soportería profesional para instalaciones industriales.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'ABRTU', 'nombre': 'Abrazadera Tipo U - Galvanizada', 'descripcion': 'Abrazadera en forma de U con tuercas para sujeción de tubería a superficies o estructuras. Permite desmontaje fácil.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'ABRTUP', 'nombre': 'Abrazadera Tipo U Pesada, Con Tuerca y Placa - Galvanizada', 'descripcion': 'Abrazadera U de servicio pesado con placa base y tuercas incluidas. Para tubería de gran diámetro y cargas pesadas.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'ABRCLIP', 'nombre': 'Abrazadera Tipo Clip - Galvanizada', 'descripcion': 'Abrazadera tipo clip de instalación rápida por presión. Para tubería conduit eléctrico y cables.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'MTROQ', 'nombre': 'Mordaza Troquelada - Galvanizada', 'descripcion': 'Mordaza galvanizada fabricada por troquelado para conexiones en canal Unistrut. Permite uniones en ángulo y cruce de canales.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                ],
            },
            'Elementos de Construcción': {
                'descripcion': 'Clavos, ángulos, pernos para concreto y elementos de fijación para construcción.',
                'productos': [
                    {'codigo': 'CPV', 'nombre': 'Tuerca Cople UNC - Galvanizada', 'descripcion': 'Tuerca cople (tuerca larga de unión) para empalmar dos varillas roscadas. Galvanizada para uso en exteriores.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'TRESOR', 'nombre': 'Tuerca Resorte UNC - Galvanizada', 'descripcion': 'Tuerca con resorte de retención para canal Unistrut. Se desliza dentro del canal y se fija al apretar el tornillo.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'VRGALV2', 'nombre': 'Varilla Roscada UNC - Galvanizada 3 Mt', 'descripcion': 'Varilla roscada galvanizada de 3 metros. Para colgantes de plafón, ductos y charolas en instalaciones eléctricas.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': 'UNC', 'grado': ''},
                    {'codigo': 'ANGCLA', 'nombre': 'Ángulo con Clavo para Concreto', 'descripcion': 'Ángulo metálico con clavo de acero para fijación directa en concreto. Para soportería rápida de tubería y ductos.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'CLAR', 'nombre': 'Clavo con Rondana', 'descripcion': 'Clavo de acero con rondana integrada para fijación de láminas, tela asfáltica y fieltro. Cabeza ancha evita desgarres.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'CLAPCON', 'nombre': 'Clavo para Concreto', 'descripcion': 'Clavo de acero endurecido para penetración directa en concreto y mampostería. Para fijaciones ligeras sin necesidad de taladro.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'PERCON', 'nombre': 'Perno para Concreto', 'descripcion': 'Perno de anclaje para fijación estructural en concreto. Para bases de maquinaria, postes, columnas y estructuras pesadas.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': '', 'destacado': True},
                ],
            },
        },
    },
    # =====================================================================
    # 10. ESTRUCTURAL
    # =====================================================================
    'Estructural': {
        'icono': 'estructural',
        'descripcion': 'Tornillería estructural de alta resistencia para conexiones en acero conforme a normas ASTM.',
        'orden': 10,
        'subcategorias': {
            'Pernos y Tornillos Estructurales': {
                'descripcion': 'Pernos estructurales A325 y accesorios para conexiones de acero en edificaciones.',
                'productos': [
                    {'codigo': 'FCELSDN', 'nombre': 'Perno Nelson Automotriz', 'descripcion': 'Perno Nelson (stud) para soldadura de conectores de corte en vigas compuestas acero-concreto. Transfiere esfuerzos cortantes entre la losa y la viga.', 'material': 'acero', 'acabado': 'sin_acabado', 'norma': '', 'grado': '', 'destacado': True},
                    {'codigo': 'EASRREL', 'nombre': 'Fémula / Fémula Cerámica para Perno Nelson', 'descripcion': 'Férula cerámica protectora para soldadura de pernos Nelson. Contiene la soldadura fundida y forma el collarín de refuerzo.', 'material': 'otro', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'T2HIC', 'nombre': 'Tuerca Hexagonal 2H UNC Estándar GC Pavonada', 'descripcion': 'Tuerca pesada 2H norma ASTM A194 para uso con pernos A325. Galvanizada por inmersión en caliente para estructuras exteriores.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': '2H'},
                    {'codigo': 'RH436', 'nombre': 'Rondana F436 UNC Estándar GC', 'descripcion': 'Rondana endurecida F436 para conexiones estructurales. Requerida por norma en juntas de alta resistencia con pernos A325/A490.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'F436'},
                    {'codigo': 'RH436GC', 'nombre': 'Rondana F436 UNC Estándar - 1 Metro Pavonada', 'descripcion': 'Rondana estructural F436 con acabado pavonado estándar. Dureza controlada para distribución uniforme de carga.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'UNC', 'grado': 'F436'},
                ],
            },
        },
    },
    # =====================================================================
    # 11. AUTOMOTRIZ
    # =====================================================================
    'Automotriz': {
        'icono': 'automotriz',
        'descripcion': 'Birlos, tuercas, rondanas y grapas para servicio automotriz ligero y pesado.',
        'orden': 11,
        'subcategorias': {
            'Servicio Ligero': {
                'descripcion': 'Birlos, tuercas y rondanas para vehículos ligeros: autos, camionetas y SUVs.',
                'productos': [
                    {'codigo': 'BIRLOSTD', 'nombre': 'Birlo Estándar para Rin', 'descripcion': 'Birlo de rueda estándar para vehículos ligeros. Rosca prensada de alta resistencia para fijación segura de rines.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'BIRLOMM', 'nombre': 'Birlo Milimétrico', 'descripcion': 'Birlo de rueda con rosca milimétrica para vehículos con especificaciones métricas (europeos, asiáticos). Diferentes largos y pasos disponibles.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'BIRLOMIX', 'nombre': 'Birlo Milimétrico Mixto', 'descripcion': 'Birlo con rosca mixta (dos pasos diferentes) para adaptación de rines de aluminio en mazas originales. Solución para conversiones de rines.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'BIRLOFL', 'nombre': 'Birlo Flecha', 'descripcion': 'Birlo tipo flecha para fijación de flechas y juntas homocinéticas. Rosca de alta resistencia para componentes de transmisión.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'CONOAUT', 'nombre': 'Cono para Birlo', 'descripcion': 'Cono adaptador para birlos de rin. Permite usar birlos estándar en rines con asiento cónico de diferente ángulo.', 'material': 'acero', 'acabado': 'cromado', 'norma': '', 'grado': ''},
                    {'codigo': 'TAPONAUTO', 'nombre': 'Tapón para Birlo', 'descripcion': 'Tapón decorativo plástico o cromado para cubrir la cabeza del birlo. Mejora la estética del rin y protege la rosca.', 'material': 'plastico', 'acabado': 'cromado', 'norma': '', 'grado': ''},
                    {'codigo': 'TUERLUJ', 'nombre': 'Tuerca de Lujo Cromada', 'descripcion': 'Tuerca cromada decorativa para rines de aluminio deportivos. Acabado espejo de alta durabilidad.', 'material': 'acero', 'acabado': 'cromado', 'norma': '', 'grado': ''},
                    {'codigo': 'TUERBSEG', 'nombre': 'Tuerca y Birlo de Seguridad', 'descripcion': 'Kit antirrobo con birlo y tuerca de seguridad con llave única. Protege los rines contra robo con patrón exclusivo.', 'material': 'acero', 'acabado': 'cromado', 'norma': '', 'grado': '', 'destacado': True},
                ],
            },
            'Servicio Pesado': {
                'descripcion': 'Birlos, tuercas y componentes para vehículos pesados: camiones, tráilers y autobuses.',
                'productos': [
                    {'codigo': 'BIRLOSP', 'nombre': 'Birlo Servicio Pesado', 'descripcion': 'Birlo de rueda para camión y tráiler. Acero de alta resistencia para las exigencias del transporte de carga pesada.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'BIRLOART', 'nombre': 'Birlo de Artillería', 'descripcion': 'Birlo tipo artillería para rines de camión con diseño de múltiples agujeros. Rosca izquierda o derecha según posición.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'ABRAZMARIP', 'nombre': 'Abrazadera Mariposa para Camión', 'descripcion': 'Abrazadera tipo mariposa para escape y sistemas de admisión en camiones. Apriete uniforme en conexiones de gran diámetro.', 'material': 'acero', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'CENTMUELLE', 'nombre': 'Centro de Muelle', 'descripcion': 'Perno central para paquete de muelles de suspensión de camión. Mantiene alineadas las hojas del resorte.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'TUERCAPCHN', 'nombre': 'Tuerca Capuchón para Camión', 'descripcion': 'Tuerca con capuchón protector para birlos de camión. Protege la rosca y mejora la apariencia del rin.', 'material': 'acero', 'acabado': 'cromado', 'norma': '', 'grado': ''},
                ],
            },
            'Grapas y Clips Automotrices': {
                'descripcion': 'Clips de fijación, retención, montaje y tapicería para carrocería automotriz.',
                'productos': [
                    {'codigo': 'CLIPFIJ', 'nombre': 'Clips de Fijación y Retención', 'descripcion': 'Clips plásticos de fijación rápida para paneles de carrocería, molduras y cubiertas. Compatible con múltiples marcas automotrices.', 'material': 'plastico', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'CLIPMONT', 'nombre': 'Clips de Montaje', 'descripcion': 'Clips metálicos tipo speed nut para montaje rápido de componentes automotrices. Se instalan a presión sin herramientas.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'CLIPTAP', 'nombre': 'Clips de Tapicería', 'descripcion': 'Clips plásticos para fijación de tapicería interior, cielo, alfombras y paneles de puerta. Diseño de expansión por presión.', 'material': 'plastico', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'CLIPSUJ', 'nombre': 'Clips de Sujeción', 'descripcion': 'Clips de sujeción universales para arneses eléctricos, mangueras y cables en el compartimento del motor.', 'material': 'plastico', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'CONMANG', 'nombre': 'Conector de Manguera', 'descripcion': 'Conector rápido para mangueras de vacío, combustible y refrigerante. Conexión segura sin herramientas.', 'material': 'plastico', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'CLIPMOLD', 'nombre': 'Clips para Molduras', 'descripcion': 'Clips especializados para retener molduras laterales, de parabrisas y de defensa. Diseño específico por marca y modelo.', 'material': 'plastico', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'REMCIEGO', 'nombre': 'Remaches Ciegos (Pop)', 'descripcion': 'Remaches de tracción tipo pop en aluminio y acero. Para uniones permanentes en lámina, plásticos y materiales delgados sin acceso al reverso.', 'material': 'otro', 'acabado': 'otro', 'norma': '', 'grado': '', 'destacado': True},
                    {'codigo': 'TORNAILON', 'nombre': 'Tornillo de Nailon', 'descripcion': 'Tornillo de nylon (plástico) para fijaciones que requieren aislamiento eléctrico o donde no se desea corrosión ni conductividad.', 'material': 'nylon', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'TOPEHULE', 'nombre': 'Tope de Hule', 'descripcion': 'Tope amortiguador de hule para capot, cajuela y puertas. Absorbe impactos y reduce ruido de cierre.', 'material': 'hule', 'acabado': 'otro', 'norma': '', 'grado': ''},
                ],
            },
        },
    },
    # =====================================================================
    # 12. FERRETERÍA GENERAL
    # =====================================================================
    'Ferretería General': {
        'icono': 'ferreteria',
        'descripcion': 'Herramientas, brocas, llaves, cintas y accesorios generales de ferretería para taller y hogar.',
        'orden': 12,
        'subcategorias': {
            'Herramientas y Accesorios': {
                'descripcion': 'Brocas, llaves, cintas adhesivas y herramientas auxiliares de ferretería.',
                'productos': [
                    {'codigo': 'BROCON', 'nombre': 'Broca para Concreto', 'descripcion': 'Broca con punta de carburo de tungsteno para perforación en concreto, block y tabique. Compatible con taladros de percusión y rotomartillos.', 'material': 'acero', 'acabado': 'otro', 'norma': '', 'grado': '', 'destacado': True},
                    {'codigo': 'BROCMET', 'nombre': 'Broca A/V para Metal', 'descripcion': 'Broca de alta velocidad (HSS) para perforación en acero, hierro y metales no ferrosos. Punta afilada a 118° para inicio preciso.', 'material': 'acero', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'LLAHEX', 'nombre': 'Llave Hexagonal L Fraccional', 'descripcion': 'Llave Allen en L (pulgadas) para tornillos con hueco hexagonal. Acero al cromo-vanadio para máxima durabilidad.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'LLAHEXMM', 'nombre': 'Llave Hexagonal L Milimétrica', 'descripcion': 'Llave Allen en L con medidas milimétricas. Indispensable para tornillos Allen métricos en maquinaria y equipos importados.', 'material': 'acero', 'acabado': 'pavonado', 'norma': 'Milimétrico', 'grado': ''},
                    {'codigo': 'PRHLLPS', 'nombre': 'Punta Phillips', 'descripcion': 'Punta de inserción Phillips para desarmador de puntas intercambiables y taladro. Acero endurecido S2 de larga duración.', 'material': 'acero', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'ROLDLO', 'nombre': 'Dados Magnéticos', 'descripcion': 'Dado magnético para taladro que sujeta la tuerca o tornillo hexagonal durante el atornillado. Agiliza el trabajo en altura y espacios difíciles.', 'material': 'acero', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'DADO', 'nombre': 'Dados de Impacto', 'descripcion': 'Dados de impacto de cromo-molibdeno para pistolas neumáticas e hidráulicas. Resisten el golpeteo sin fracturarse.', 'material': 'acero', 'acabado': 'pavonado', 'norma': '', 'grado': ''},
                    {'codigo': 'CENMP', 'nombre': 'Cinta Adhesiva Acrílica BOPP', 'descripcion': 'Cinta de empaque transparente de polipropileno con adhesivo acrílico. Para sellado de cajas y embalaje general.', 'material': 'plastico', 'acabado': 'otro', 'norma': '', 'grado': ''},
                    {'codigo': 'ALC', 'nombre': 'Armella Cerrada - Galvanizada', 'descripcion': 'Armella de ojo cerrado galvanizada para colgar objetos, pasar cables y crear puntos de amarre. Rosca autorroscante para madera.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                    {'codigo': 'ARMECR', 'nombre': 'Armella Abierta - Galvanizada', 'descripcion': 'Armella de gancho abierto para colgar cuadros, plantas y accesorios ligeros. Fácil de instalar en madera y tablaroca con taquete.', 'material': 'galvanizado', 'acabado': 'galvanizado', 'norma': '', 'grado': ''},
                ],
            },
        },
    },
}


class Command(BaseCommand):
    help = 'Carga el catálogo completo de productos de Tornillos del Sur'

    def handle(self, *args, **options):
        productos_creados = 0
        for cat_nombre, cat_data in CATALOGO.items():
            categoria, _ = Categoria.objects.update_or_create(
                nombre=cat_nombre,
                defaults={
                    'descripcion': cat_data['descripcion'],
                    'icono': cat_data.get('icono', ''),
                    'orden': cat_data.get('orden', 0),
                },
            )
            self.stdout.write(f'  Categoría: {categoria.nombre}')

            for sub_nombre, sub_data in cat_data['subcategorias'].items():
                subcategoria, _ = SubCategoria.objects.update_or_create(
                    categoria=categoria,
                    nombre=sub_nombre,
                    defaults={
                        'descripcion': sub_data.get('descripcion', ''),
                    },
                )
                self.stdout.write(f'    Subcategoría: {subcategoria.nombre}')

                for prod_data in sub_data['productos']:
                    _, created = Producto.objects.update_or_create(
                        codigo=prod_data['codigo'],
                        defaults={
                            'subcategoria': subcategoria,
                            'nombre': prod_data['nombre'],
                            'descripcion': prod_data.get('descripcion', ''),
                            'material': prod_data.get('material', ''),
                            'acabado': prod_data.get('acabado', ''),
                            'norma': prod_data.get('norma', ''),
                            'grado': prod_data.get('grado', ''),
                            'destacado': prod_data.get('destacado', False),
                        },
                    )
                    if created:
                        productos_creados += 1

        total_cats = Categoria.objects.count()
        total_subs = SubCategoria.objects.count()
        total_prods = Producto.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'\nCatálogo cargado: {total_cats} categorías, {total_subs} subcategorías, {total_prods} productos ({productos_creados} nuevos)'
        ))
