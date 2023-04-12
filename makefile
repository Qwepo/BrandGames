run:
	docker-compose  up  -d
	sleep 5
	pip install -r requirements.txt
	./manage.py makemigrations
	./manage.py migrate
	
