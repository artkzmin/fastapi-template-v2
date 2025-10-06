run:
	uv run python -m src.main
pre-commit:
	uv run pre-commit run --all-files
revision:
	uv run alembic revision --autogenerate -m "temp"
migrate:
	uv run alembic upgrade head
docker-run:
	docker compose -f docker/docker-compose.yml up --build -d
