#!/bin/bash

if [[ ! -d "venv" ]]
then 
	echo "Cration of the virtual environement"
	virtualenv venv
	virtualenv -p /usr/bin/python3 venv
	python3 -m pip freeze > requirements.txt
	python3 -m pip install -r requirements.txt
fi

if [[ -d "venv" ]]
then
	echo "Activation"
	source venv/bin/activate
fi

chmod +x main.py
./main.py
