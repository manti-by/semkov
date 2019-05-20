local:
	python ./app/manage.py runserver

migrate:
	python ./app/manage.py migrate

migration:
	python ./app/manage.py makemigrations

messages:
	python ./app/manage.py makemessages

compile-messages:
	python ./app/manage.py compilemessages

venv:
	virtualenv -p $(shell which python3) --no-site-packages --prompt='smk-' ../venv

pip:
	pip install -Ur deploy/requirements/dev.txt

ci:
	circleci build

check:
	black -t py37 app/
	isort app/*.py
	flake8


get-db:
	scp amon-ra:/home/manti/www/sg.manti.by/src/app/db.sqlite3 app/db.sqlite3

upload-db:
	scp app/db.sqlite3 amon-ra:/home/manti/www/sg.manti.by/src/app/db.sqlite3


build:
	docker build -f deploy/Dockerfile -t mantiby/semkov:latest deploy/

start:
	docker-compose -f deploy/docker-compose.yml up -d

stop:
	docker-compose -f deploy/docker-compose.yml stop

restart:
	stop start

destroy:
	docker-compose -f deploy/docker-compose.yml down

static:
	docker exec -it semkov-app python manage.py collectstatic --no-input

bash:
	docker exec -it semkov-app bash

send_email:
	docker exec -it semkov-app python manage.py send_email
