PROJECT_VERSION := $(shell chmod +x cli/get_project_version.sh; cli/get_project_version.sh)

run:
	uv run python -m src.main
format:
	uv run pre-commit run --all-files
revision:
	uv run alembic revision --autogenerate -m "$(PROJECT_VERSION)"
migrate:
	uv run alembic upgrade head
build:
	docker network create ${PROJECT__NAME}-network
	docker compose -f docker/docker-compose.yml \
		--env-file=config/.env \
		up --build -d
coverage:
	coverage run -m pytest
	coverage report
test:
	pytest -v -s
cloc:
	git ls-files | xargs cloc
set-project-name:
	chmod +x cli/set_project_name.sh
	cli/set_project_name.sh
cp-env:
	cp config/.env.dist config/.env
	cp config/.test.env.dist config/.test.env
