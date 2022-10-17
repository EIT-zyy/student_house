# student_house

## This is a project that you can learn django of Python
The whole project is on django framework, and build an student management system.

## Enviroment

```
mkdir testenv
cd testenv
virtualenv student_env
source student_env/bin/activate
pip3 install django~=1.11
mkdir workspace
cd workspace
mkdir student_house
cd student_house && django-admin startproject student_sys
cd student_sys/student_sys/
python manage.py  makemigrations
python manage.py migrate
python manage.py createsuperuser
```

## Thanks for the5fire book 《Django 企业开发实战》
How to make a wev server?
You just can run:

```
cd student_sys
python manage.py runserver
```
