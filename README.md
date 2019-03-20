# Semkov Gorodok blog  

[![CircleCI](https://img.shields.io/circleci/project/bitbucket/manti_by/semkov/master.svg)](https://circleci.com/bb/manti_by/semkov)
[![Docker](https://img.shields.io/docker/cloud/build/mantiby/semkov.svg)](https://hub.docker.com/r/mantiby/semkov/)

## About  

[![Code style: black](https://img.shields.io/badge/wagtail-2.4-green.svg)](https://pypi.org/project/wagtail/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://bitbucket.org/manti_by/semkov/raw/c61190bd891b532908a64fdbdb1cd53a7f259c87/LICENSE)  

Author: Alexander Chaika <manti.by@gmail.com>  

Source link: https://bitbucket.org/manti_by/semkov/  

Requirements: Docker, Python 3.5+, SQLite  


## Setup development environment  

1. Install python pip

        $ sudo apt install python-pip sqlite3

2. Install, create and activate virtualenv

        $ sudo pip install virtualenv  
        $ virtualenv -p python3 --no-site-packages --prompt=smk- venv  
        $ source venv/bin/activate  

3. Clone sources and install pip packages

        $ mkdir semkov/ && cd semkov/  
        $ git clone https://bitbucket.org/manti_by/semkov.git src && cd src/  
        $ pip install -r deploy/requirements/dev.txt  

4. Run local dev server or prod server

        $ make local  


**NOTICE**: Before pushing your changes, run next commands

    $ make check
    $ make ci


## Run in production

To run app in production mode, clone repo, run docker and collect static

    $ git clone https://manti_by@bitbucket.org/manti_by/semkov.git
    $ cd semkov/ && make prod
    $ make static