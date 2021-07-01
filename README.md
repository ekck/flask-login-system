# flask-login-system
Simple but gets the job done right.



## Requirements 
[environment]
source env/bin/activate

pipenv install -r ./requirements.txt

[requires]
- python v2.7.18 or  
- python3 v3.8

[packages]
- flask = "*"
- flask-login = "*"
- flask-sqlalchemy = "*"

[export]
- export FLASK_APP=app.py
- export FLASK_DEBUG=True

[create_db]
- python 
- from app import db
- db.create_all() exit()

- flask run



