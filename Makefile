build:
	docker-compose build

up:
	docker-compose up -d

up-non-daemon:
	docker-compose up

start:
	docker-compose start

stop:
	docker-compose stop

restart:
	docker-compose stop && docker-compose start

shell-nginx:
	docker exec -ti nz02 /bin/sh

shell-web:
	docker exec -ti dz02 /bin/sh

shell-db:
	docker exec -ti pz02 /bin/sh

log-nginx:
	docker-compose logs nginx  

log-web:
	docker-compose logs web  

log-db:
	docker-compose logs db

collectstatic:
	docker exec dz02 /bin/sh -c "python manage.py collectstatic --noinput"  