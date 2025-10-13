FROM python:3.11.9

WORKDIR /app

RUN pip install uv

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

COPY alembic.ini alembic.ini
COPY Makefile Makefile

COPY config/.env config/.env

COPY src/ src/

CMD ["make", "run"]