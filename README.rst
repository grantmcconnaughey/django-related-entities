=============================
django-related-entities
=============================

.. image:: https://badge.fury.io/py/django-related-entities.png
    :target: https://badge.fury.io/py/django-related-entities

.. image:: https://travis-ci.org/grantmcconnaughey/django-related-entities.png?branch=master
    :target: https://travis-ci.org/grantmcconnaughey/django-related-entities

Generically relate any two model objects in Django.

Documentation
-------------

The full documentation is at https://django-related-entities.readthedocs.org.

Quickstart
----------

Install django-related-entities::

    pip install django-related-entities

Add the 'relatedentities' package to your INSTALLED_APPS::

    INSTALLED_APPS = (
        # ...
        'relatedentities',
        # ...
    )

Be sure to run migrations::

    python manage.py migrate

Features
--------

* Easily create generic relationships between any two models in your database.
* Handy when used for authorization.

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
