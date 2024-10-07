
python manage.py runserver 0.0.0.0:8000 &
sleep 10
celery -A seu_app worker --loglevel=info --noinput