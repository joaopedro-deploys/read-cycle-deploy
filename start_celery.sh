#!/bin/bash
nohup celery -A your_app_name worker --loglevel=info > celery.log 2>&1 &
