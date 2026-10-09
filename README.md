# Week 3 Project: Task Tracker

Django task tracker with Users, Projects, Tasks and Comments, plus Django REST Framework CRUD endpoints for Tasks.

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py check
python manage.py createsuperuser
python manage.py runserver
```

Admin: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/api/tasks/

The Task admin supports title search and project filtering. The API supports GET, POST, PUT, PATCH and DELETE for tasks using a DRF ModelSerializer and ModelViewSet.
