rundb:
	docker-compose  up  -d
	pip install -r requirements.txt
	./manage.py makemigrations
	./manage.py migrate
