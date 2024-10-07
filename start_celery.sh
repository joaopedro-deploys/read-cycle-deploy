#!/bin/bash
# Aguardar alguns segundos para garantir que o App Service esteja inicializado

python manage.py runserver 0.0.0.0:8000

sleep 30
celery -A project worker --pool=solo -l info