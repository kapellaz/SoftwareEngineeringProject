# Ativar virtual environment

$ cd Desktop

$ source kahucvenv/bin/activate

---
# Desativar virtual environment
$ deactivate

---
# Correr aplicação
$ cd kahuc/DEV/kahucsite

## Modo development:
$ gunicorn -c gunicorn_dev.py

## Modo production:
$ gunicorn -c gunicorn_prod.py

---
# Terminar servidor
$ pkill gunicorn

---
# Ver log

## Log de development:
$ tail -f /var/log/gunicorn/dev.log

## Log de production:
$ tail -f /var/log/gunicorn/prod.log
