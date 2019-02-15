Semkov
====


About
----

Semkov Gorodok homepage 

Author: Alexander Chaika <manti.by@gmail.com>

Source link: https://bitbucket.org/manti_by/semkov/

Requirements:

    Python 3+, SQLite


Setup
----

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

