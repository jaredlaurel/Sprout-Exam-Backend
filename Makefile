.DEFAULT_TARGET: build
.PHONY: start start_deps stop remove

service := $(service)

build:
	docker-compose -f docker-compose.yaml up --force-recreate -d --build

run:
	docker-compose -f docker-compose.yaml up -d

stop:
	docker-compose -f docker-compose.yaml stop

logs:
	docker-compose logs -f

remove:
	docker-compose -f docker-compose.yaml down
