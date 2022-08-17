#!/bin/sh
# This script is executed by the Docker container on startup.

# Run database migrations.
python manage.py migrate --noinput

# Start the server.
python manage.py runserver 0.0.0.0:8000