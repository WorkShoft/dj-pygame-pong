runclient:
	python client/main.py

runserver:
	python server/manage.py runserver

test:
	pytest client/tests.py

makemigrations:
	python server/manage.py makemigrations

migrate:
	python server/manage.py migrate
