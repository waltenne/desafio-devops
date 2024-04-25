# Makefile api

dbup:
	docker compose -f ./app/compose/compose-db.yml up

dbdown:
	docker compose -f ./app/compose/compose-db.yml down

devup:
	docker compose -f ./app/compose/compose-dev.yml up

devdown:
	docker compose -f ./app/compose/compose-dev.yml down