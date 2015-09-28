#!/usr/bin/env python
# Convenience script to do things like run ./manage.py makemigrations
import os
import sys

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

    from django.conf import settings
    from django.test.utils import get_runner

    settings.configure(
        DEBUG=True,
        USE_TZ=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        ROOT_URLCONF="relatedentities.urls",
        INSTALLED_APPS=[
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "django.contrib.sites",
            "relatedentities",
            "tests",
        ],
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(),
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
