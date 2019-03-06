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
	docker build --no-cache -f deploy/Dockerfile -t mantiby/semkov:latest deploy/

start:
	docker run -p 8898:8898 --name semkov -v $(pwd)/app/static:/var/static -v $(pwd)/app/media:/var/media mantiby/semkov:latest

stop:
	docker stop semkov

destroy:
	docker rm semkov

static:
	docker exec -it semkov python manage.py collectstatic --no-input

bash:
	docker exec -it semkov bash

check:
	black --py36 app/
	isort app/*.py
	flake8
