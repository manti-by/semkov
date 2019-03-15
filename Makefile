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
	docker-compose -f deploy/docker-compose.yml up -d

stop:
	docker-compose -f deploy/docker-compose.yml stop

destroy:
	docker-compose -f deploy/docker-compose.yml down

static:
	docker exec -it semkov-app python manage.py collectstatic --no-input

bash:
	docker exec -it semkov-app bash

send_email:
	docker exec -it semkov-app python manage.py send_email

ci:
	circleci build

check:
	black --py36 app/
	isort app/*.py
	flake8
