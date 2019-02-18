local:
	../venv/bin/python ./app/manage.py runserver

check:
	black --py36 app/
	isort app/*.py
	flake8