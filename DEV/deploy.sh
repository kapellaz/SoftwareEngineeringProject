#!/bin/bash/

# Apaga tabelas da DB
# PGPASSWORD='megapassdokahuc' psql -U kahucsite -h 127.0.0.1 -d kahuc_db -c "select table_name from information_schema.tables where table_schema = 'public';"
PGPASSWORD='megapassdokahuc' psql -U kahucsite -h 127.0.0.1 -d kahuc_db -c "select 'drop table if exists ' || tablename || ' cascade;' from pg_tables where schemaname = 'public';" | sed '1d;2d;$d;' > drop_tables.sql
PGPASSWORD='megapassdokahuc' psql -U kahucsite -h 127.0.0.1 -d kahuc_db < drop_tables.sql
# PGPASSWORD='megapassdokahuc' psql -U kahucsite -h 127.0.0.1 -d kahuc_db -c "select table_name from information_schema.tables where table_schema = 'public';"
rm drop_tables.sql

source ~/Desktop/kahucvenv/bin/activate
cd ~/Desktop/kahuc/DEV/kahucsite

# Apaga migracoes anteriores
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# Migra modelos para a DB
dirs=(!(kahucsite|static|templates)/)
dirs="$(echo \"${dirs[*]}\" | sed 's#/##g')"  # remove barras dos nomes dos diretorios
dirs="${dirs%\"}"                             # remove aspa esquerda da string
dirs="${dirs#\"}"                             # remove aspa direita da string

python3 manage.py makemigrations $dirs # TODO: automatizar migracao de apps que nao tenha diretorio migrations
python3 manage.py migrate
python3 manage.py shell < create_kahuc_groups.py

PGPASSWORD='megapassdokahuc' psql -U kahucsite -h 127.0.0.1 -d kahuc_db -c "select table_name from information_schema.tables where table_schema = 'public';"

# Recolhe ficheiros estaticos para servicing
yes 'yes' | python3 manage.py collectstatic --clear

PGPASSWORD='megapassdokahuc' psql -U kahucsite -h 127.0.0.1 -d kahuc_db < ~/Desktop/kahuc/DEV/testing/insertData.sql

unset dirs

cd ~/Desktop/kahuc/DEV
