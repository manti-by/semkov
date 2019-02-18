# Semkov Gorodok blog  

[![Code style: black](https://img.shields.io/badge/wagtail-2.4-green.svg)](https://pypi.org/project/wagtail/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License](https://img.shields.io/badge/license-BSD-blue.svg)](https://bitbucket.org/manti_by/semkov/raw/1b21fb9955126a4d43d5fe996ef9ed30a4b4eec6/LICENSE)  


## About  

Author: Alexander Chaika <manti.by@gmail.com>  

Source link: https://bitbucket.org/manti_by/semkov/  

Requirements: Docker, Python 3.5+, SQLite  


## Setup  

1. Install python pip

        $ sudo apt install python-pip sqlite3 supervisor  

2. Install, create and activate virtualenv

        $ sudo pip install virtualenv  
        $ virtualenv -p python3 --no-site-packages --prompt=smk- venv  
        $ source venv/bin/activate  

3. Clone sources and install pip packages

        $ mkdir semkov/ && cd semkov/  
        $ git clone https://bitbucket.org/manti_by/semkov.git src && cd src/  
        $ pip install -r deploy/requirements.txt  

4. Run local dev server or prod server

        $ make local  
        $ make prod