# Semkov Gorodok blog

## About

[![Wagtail 5.2.2](https://img.shields.io/badge/wagtail-5.2.2-green.svg)](https://pypi.org/project/wagtail/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://bitbucket.org/manti_by/semkov/raw/c61190bd891b532908a64fdbdb1cd53a7f259c87/LICENSE)

Author: Alexander Chaika <manti.by@gmail.com>

Source link: https://github.com/manti-by/semkov

Requirements: Docker, Python 3.11, PostgreSQL


## Setup development environment

1. Create and activate virtualenv

    ```shell
    virtualenv .venv
    source .venv/bin/activate
    ```

2. Clone sources and install pip packages

    ```shell
    git clone git@github.com:manti-by/semkov.git .
    pip install -r requirements.txt
    ```

3. Run migration and local dev server

    ```shell
    python manage.py migrate
    python manage.py runserver
    ```

**NOTICE**: Before pushing your changes, run the next commands

```shell
make django-check
make check
make test
```

## Run in production

To run app in production mode, clone repo, build image and run it

```shell
git clone git@github.com:manti-by/semkov.git .
make build
docker compose up -d
make migrate
make static
```
