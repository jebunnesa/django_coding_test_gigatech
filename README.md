# django_coding_test_gigatech
created for django coding test

# The first thing to do is to clone the repository:

$ git clone https://github.com/jebunnesa/django_coding_test_gigatech.git


# Create a virtual environment to install dependencies in and activate it:

$ python3 -m venv venv
$ source venv/bin/activate

# Then install the dependencies:

(venv)$ pip3 install -r requirements.txt

# Database

update your database credentials to seetings.py  (postgresql Database is used)
and do migrate,
(venv)$ python3 manage.py migrate

# Run Project:
(venv)$ python3 manage.py runserver


