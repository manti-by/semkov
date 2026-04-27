build:
	docker build -t mantiby/semkov:latest .

deploy:
	docker container stop semkov-wagtail
	docker container rm semkov-wagtail
	docker compose up -d

static:
	docker exec -it semkov-wagtail python manage.py collectstatic --no-input

migrate:
	docker exec -it semkov-wagtail python manage.py migrate

bash:
	docker exec -it semkov-wagtail bash

send_email:
	docker exec -it semkov-wagtail python manage.py send_email

dump:
	docker exec -it semkov-postgres pg_dump -U semkov -d semkov > /mnt/data/www/semkov/data/database.sql

restore:
	docker cp /mnt/data/www/semkov/data/database.sql semkov-postgres:/tmp/database.sql
	docker exec -it semkov-postgres psql -U semkov semkov -f /tmp/database.sql

update-data:
	uv run manage.py update_transport
	uv run manage.py update_positions

upload-data:
	scp -r /mnt/data/www/semkov/media/ amon-ra:/mnt/data/www/semkov/
	scp -r /mnt/data/www/semkov/data/ amon-ra:/mnt/data/www/semkov/

download-data:
	scp -r amon-ra:/mnt/data/www/semkov/media/ /mnt/data/www/semkov/
	scp -r amon-ra:/mnt/data/www/semkov/data/ /mnt/data/www/semkov/

update:
	uv run uv-bump
	uv sync --all-extras --dev
	uv run pre-commit autoupdate

pip:
	uv sync --all-extras --dev

test:
	uv run pytest --create-db --disable-warnings --ds=semkov.settings.test semkov/

check:
	git add .
	uv run pre-commit run

django-check:
	uv run manage.py makemigrations --dry-run --check --verbosity=3 --settings=semkov.settings.test
	uv run manage.py check --fail-level WARNING --settings=semkov.settings.test

ci: pip check django-check test
