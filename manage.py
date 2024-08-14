#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Spuštění administrativních úloh."""
    # Nastaví výchozí modul nastavení pro Django projekt
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ambulance.settings')
    try:
        # Pokusí se importovat funkci execute_from_command_line z django.core.management
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Vyvolá výjimku, pokud nelze Django importovat
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Spustí Django příkazový řádek s argumenty, které jsou předány při spuštění skriptu
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Spustí funkci main pouze v případě, že skript je spuštěn jako hlavní program
    main()
