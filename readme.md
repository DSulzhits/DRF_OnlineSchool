Project Online_School, created with Django-DRF, also added integration with Docker

FOR LOCAL AND FOR REDIS
Activate virtual environment
```bash
python3 -m venv venv
```

Install dependencies from file: `requirements.txt`
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

Apply migrations
```bash
python manage.py migrate
```

Retrieve data from fixtures
```bash
python manage.py loaddata data_users.json
python manage.py loaddata data_courses.json
```

FOR LOCAL
Start, and check redis (if redis started you retrieve answer "pong")
```bash
redis-server
redis-cli ping
```

Start, project 
```bash
python manage.py runserver
```


FOR DOCKER
Create docker image
```bash
 docker-compose build
```

Start docker image
```bash
 docker-compose up
```
__________________________________________