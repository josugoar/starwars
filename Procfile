web: gunicorn traveloffers.wsgi

release: ./manage.py migrate --no-input
release: ./manage.py loaddata offers.json
