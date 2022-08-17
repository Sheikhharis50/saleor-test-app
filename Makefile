DFLAGS= 

bootstrap:
	docker-compose build
	docker-compose run --rm api python3 manage.py migrate
	docker-compose run --rm api python3 manage.py collectstatic --noinput
run:
	docker-compose up $(DFLAGS)
kill:
	docker-compose down