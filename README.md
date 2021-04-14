# Semkov Gorodok blog  

## About  

[![Wagtail 2.12](https://img.shields.io/badge/wagtail-2.12-green.svg)](https://pypi.org/project/wagtail/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://bitbucket.org/manti_by/semkov/raw/c61190bd891b532908a64fdbdb1cd53a7f259c87/LICENSE)

Author: Alexander Chaika <manti.by@gmail.com>

Source link: https://github.com/manti-by/semkov

Requirements: Docker, Python 3.9, SQLite  


## Setup development environment  

1. Install virtualenv and sqlite3

        $ sudo apt install virtualenv sqlite3

2. Install, create and activate virtualenv

        $ pip install virtualenv  
        $ virtualenv -p python3 --no-site-packages --prompt=smk- venv
        $ source venv/bin/activate  

3. Clone sources and install pip packages
  
        $ git clone git@github.com:manti-by/semkov.git && cd semkov/
        $ pip install -r requirements/dev.txt

4. Run migration and local dev server

        $ python manage.py migrate
        $ python manage.py runserver


**NOTICE**: Before pushing your changes, run next commands

    $ make check


## Run in production

To run app in production mode, clone repo, build image and run it

    $ git clone git@github.com:manti-by/semkov.git && cd semkov/
    $ make build
    $ docker-compose up -d
    $ make migrate static