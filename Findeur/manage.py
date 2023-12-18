#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Findeur.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    args = sys.argv
    if os.system('/usr/bin/cli --cleanup') != 0:
        raise Exception('****** Another django instance is running, most likely by one of your team members, stop it first ******')
    if len(args) >= 2 and args[1] == 'runserver':
        args = [args[0], args[1], '0.0.0.0:8000']
    execute_from_command_line(args)


if __name__ == '__main__':
    main()
