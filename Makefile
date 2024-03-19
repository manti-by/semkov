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

dump:
	docker exec -it semkov-postgres pg_dump -U semkov -d semkov > database.sql

restore:
	docker cp database.sql semkov-postgres:/tmp/database.sql
	docker exec -it semkov-postgres psql -U semkov semkov -f /tmp/database.sql

update-requirements:
	pcu requirements.txt -u

update-data:
	./manage.py update_transport
	./manage.py update_positions

test:
	pytest --create-db --disable-warnings --ds=semkov.settings.test semkov/

check:
	git add .
	pre-commit run

django-check:
	./manage.py makemigrations --dry-run --check --verbosity=3 --settings=semkov.settings.test
	./manage.py check --fail-level WARNING --settings=semkov.settings.test
