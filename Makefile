PROJECT_VERSION := $(shell cli/get_project_version.sh)

run:
	uv run python -m src.main
lint:
	uv run pre-commit run --all-files
revision:
	uv run alembic revision --autogenerate -m "$(PROJECT_VERSION)"
migrate:
	uv run alembic upgrade head
build:
	docker compose -f docker/docker-compose.yml up --build -d
coverage:
	coverage run -m pytest
	coverage report
test:
	pytest -v -s
cloc:
	git ls-files | xargs cloc
sync:
	uv sync
set-project-name:
	chmod +x cli/set_project_name.sh
	./cli/set_project_name.sh
init:
	chmod +x cli/set_project_name.sh
	chmod +x cli/get_project_version.sh
