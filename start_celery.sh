#!/bin/bash
# Aguardar alguns segundos para garantir que o App Service esteja inicializado

python manage.py makemigrations
python manage.py migrate

exec gunicorn project.wsgi:application 

sleep 30
celery -A project worker --pool=solo -l info