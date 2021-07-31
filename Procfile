web: gunicorn --bind 0.0.0.0:$PORT Portfolio:myportfolio
python manage.py collectstatic --noinput
manage.py migrate
