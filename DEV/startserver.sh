#!/bin/bash

source ~/Desktop/kahucvenv/bin/activate
cd ~/Desktop/kahuc/DEV/kahucsite

if [[ $(ps -el | grep gunicorn) ]]; then
	echo "Server already running."
	cd ~/Desktop/kahuc/DEV
else
	gunicorn -c ~/Desktop/kahuc/DEV/kahucsite/gunicorn_prod.py
	sudo systemctl start nginx
	cd ~/Desktop/kahuc/DEV
	pkill tail
	sudo cat /dev/null > /var/log/nginx/kahuc.access.log
	sudo cat /dev/null > /var/log/nginx/kahuc.error.log
	sudo cat /dev/null > /var/log/gunicorn/prod.log
	tail -f /var/log/gunicorn/prod.log | sed "s/^/$(tput setaf 6)gunicorn:$(tput sgr0) /" & tail -n 5 -f /var/log/nginx/kahuc.access.log |sed "s/^/$(tput setaf 2)nginx_access:$(tput sgr0) /" & tail -n 5 -f /var/log/nginx/kahuc.error.log |sed "s/^/$(tput setaf 1)nginx_error:$(tput sgr0) /"
fi
