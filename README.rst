Documentation
=============

Getting Up and Running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv

Clone the repository::

    $ git clone https://github.com/sheeshmohsin/navyaproj

    $ cd navyaproj/user_roles_permissions/

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

    $ pip install -r requirements.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Run the Django ``migrate`` command::

    $ python manage.py migrate

    $ python manage.py makemigrations app

    $ python manage.py migrate app

You can now run the usual Django ``runserver`` command::

    $ python manage.py runserver

