#!/bin/sh

echo "Alembic start"
make migrate
echo "Alembic success"

echo "Python start"
make run