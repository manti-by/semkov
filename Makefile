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

update-project:
	ssh amon-ra "docker exec -i semkov-postgres pg_dump -U semkov -d semkov > /mnt/nostromo/www/semkov/data/semkov.sql"
	scp -r amon-ra:/mnt/nostromo/www/semkov/media .
	scp -r amon-ra:/mnt/nostromo/www/semkov/data .
	export PGPASSWORD=semkov && psql -h localhost -U semkov semkov -c "drop database semkov; create database semkov;"
	export PGPASSWORD=semkov && psql -h localhost -U semkov semkov -f ./data/semkov.sql

update-server:
	export PGPASSWORD=semkov && pg_dump -h localhost -U semkov -d semkov > ./data/semkov.sql
	scp -r ./media/ amon-ra:/mnt/nostromo/www/semkov/
	scp -r ./data/ amon-ra:/mnt/nostromo/www/semkov/
	ssh amon-ra "docker container stop semkov-postgres && docker container rm semkov-postgres"
	ssh amon-ra "cd ~/www/semkov-gorodok.by/ && docker-compose up -d"
	ssh amon-ra "docker cp /mnt/nostromo/www/semkov/data/semkov.sql semkov-postgres:/tmp/semkov.sql"
	ssh amon-ra "docker exec -it semkov-postgres psql -U semkov semkov -f /tmp/semkov.sql"

update-requirements:
	pcu requirements.txt -u

test:
	pytest

check:
	git add .
	pre-commit run
