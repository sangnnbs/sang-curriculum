web: gunicorn hello.wsgi --log-file - --log-level debug
python manage.py tailwind build
python manage.py collectstatic --noinput
python manage.py migrate