build:
	docker build -t mantiby/semkov:latest .

static:
	docker exec -it semkov-wagtail python manage.py collectstatic --no-input

migrate:
	docker exec -it semkov-wagtail python manage.py migrate

bash:
	docker exec -it semkov-wagtail bash

send_email:
	docker exec -it semkov-wagtail python manage.py send_email


update-requirements:
	pcu requirements.txt -u

test:
	pytest

check:
	flake8 semkov/
	black semkov/




