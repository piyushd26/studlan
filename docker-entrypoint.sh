#!/usr/bin/env sh
python manage.py migrate

rm /tmp/project-master.pid


echo Starting uwsgi.
exec uwsgi --chdir=/srv/studlan \
    --module=studlan.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=studlan.settings \
    --master --pidfile=/tmp/project-master.pid \
    --socket=127.0.0.1:8080 \
    --processes=5 \
    --harakiri=20 \
    --max-requests=5000 \
    --vacuum
