#!/bin/bash
# startup.sh - invoked by App Service to start the app
exec gunicorn --bind 0.0.0.0:8000 --workers 2 app:app

