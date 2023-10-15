.DEFAULT_TARGET: build
.PHONY: virtual_env

DESCRIPTION := $(description)
VENV = .venv

virtual_env:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate

start_deps:
	make virtual_env
	python3 -m pip install --upgrade pip
	python3 -m pip install -r ./requirements.txt

migrations: start_deps
	python3 migrate.py makemigrations $(DESCRIPTION)

migrate: start_deps
	python3 migrate.py migrate
