web: gunicorn config.wsgi --bind 0.0.0.0:$PORT
release: python manage.py migrate && python manage.py collectstatic --noinput && python manage.py cargar_catalogo && python manage.py asignar_imagenes
