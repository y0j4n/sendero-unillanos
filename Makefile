pro-run:
	docker-compose up
pro-stop:
	docker-compose stop
pro-build:
	docker-compose build
pro-migrate:
	docker-compose run --rm web ./manage.py makemigrations
	docker-compose run --rm web ./manage.py migrate
pro-requirements:
	docker-compose run --rm web pip install -r requirements.txt
pro-statics:
	docker-compose run --rm web ./manage.py collectstatic --no-input
pro-superuser:
	docker-compose run --rm web ./manage.py createsuperuser