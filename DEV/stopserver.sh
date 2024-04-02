#!/bin/bash

COUNTER=1
while [[ $(ps -el | grep gunicorn) ]]; do
	echo "$((COUNTER)) attempt"
	pkill gunicorn
	sleep 1
	let COUNTER=COUNTER+1
done

sudo systemctl stop nginx

pkill tail

deactivate
echo "Server stopped."


