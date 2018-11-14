# RIDE MY WAY API
Make new friends by sharing a ride with them.................

## Description
This **api** is built using [Flask](http://flask.pocoo.org/) microframework work with Python[](https://www.python.org/) as a language, [Flask-RESTPLus](https://flask-restplus.readthedocs.io/en/stable/) that adds support for quickly building REST APIs using Flask. It uses [Postgresql](https://www.postgresql.org/) as a database engine, [SQLALchemy](https://www.sqlalchemy.org/) for **Object Relational Mapping**, [marshmallow](https://marshmallow.readthedocs.io/en/3.0/#) library for fields serialization.

## Project set up

clone the repository
```
     $ git clone https://github.com/marthamareal/ride-my-way-flask-orm.git 
```

- check if you have python installed 
```
    $ python --version
```

- check if you have pipenv installed 
```
    $ python --version
```    

- check if you have postgres installed 
```
    $ postgres --version
``` 

- Install requirements
```
    $ pip install -r requirements.txt
``` 

- install a pipenv virtual environment
```
    $ pipenv install  
    
    or

    $ pipenv install --dev
``` 

- activate the virtual environment
```
    $ pipenv shell
``` 

- run 
``` 
    $ flask db init  # to automatically generate the migrations folder
```
**Note** if you dont have migrations folder, apply migrations
```
    $ flask db migrate 
```

**Note:** on making changes to the models, apply new migrations and update the versions
```   
    $ flask db upgrade   
```

## Start the project
```
    $ python manage.py runserver
```
