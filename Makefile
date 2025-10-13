run:
	uv run python -m src.main
lint:
	uv run pre-commit run --all-files
revision:
	uv run alembic revision --autogenerate -m "temp"
migrate:
	uv run alembic upgrade head
build:
	docker compose -f docker/docker-compose.yml up --build -d
coverage:
	alembic upgrade head; coverage run -m pytest
	coverage report
test:
	pytest -v -s
cloc:
	git ls-files | xargs cloc
sync:
	uv sync
