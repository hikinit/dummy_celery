rabbitmq:
	docker run -d --hostname rabbitmq --name rmq -p 5672:5672 -e RABBITMQ_DEFAULT_USER=user -e RABBITMQ_DEFAULT_PASS=password -e RABBITMQ_DEFAULT_VHOST=vhost rabbitmq:3-management

postgresql:
	docker run --name postgres -p 5432 -e POSTGRES_DB=db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -d postgres