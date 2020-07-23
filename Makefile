runclient:
	python client/main.py

runserver:
	python server/manage.py runserver

makemigrations:
	python server/manage.py makemigrations

migrate:
	python server/manage.py migrate
