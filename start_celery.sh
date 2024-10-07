#!/bin/bash
# Aguardar alguns segundos para garantir que o App Service esteja inicializado

python manage.py runserver --no-output --

sleep 30
nohup celery -A your_app_name worker --loglevel=info > celery.log 2>&1 &
