run:
	pip install -r requirements.txt
	./manage.py makemigrations
	./manage.py migrate
	./manage.py runserver

rundb:
	docker-compose  up  -d
