.PHONY: bootstrap migrate seed up down

bootstrap:
docker compose build

migrate:
docker compose run --rm backend alembic upgrade head

seed:
docker compose run --rm backend python app/seed.py

up:
docker compose up

down:
docker compose down -v
