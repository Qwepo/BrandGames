run:
	docker-compose  up  -d
	sleep 4
	pip install -r requirements.txt
	./manage.py makemigrations
	./manage.py migrate
	./manage.py runserver
	
