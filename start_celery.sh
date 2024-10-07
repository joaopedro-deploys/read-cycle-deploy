#!/bin/bash
# Aguardar alguns segundos para garantir que o App Service esteja inicializado

celery -A project worker --pool=solo -l info &

sleep 30