local:
	../venv/bin/python ./app/manage.py runserver

migrate:
	../venv/bin/python ./app/manage.py migrate

migration:
	../venv/bin/python ./app/manage.py makemigrations

messages:
	../venv/bin/python ./app/manage.py makemessages

compile-messages:
	../venv/bin/python ./app/manage.py compilemessages

build:
	docker build -f deploy/Dockerfile -t mantiby/semkov:latest deploy/

start:
	docker run -d -p 8000:8000 --name semkov mantiby/semkov:latest

stop:
	docker stop semkov

bash:
	docker exec -it semkov bash

check:
	black --py36 app/
	isort app/*.py
	flake8