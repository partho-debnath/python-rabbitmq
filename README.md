# Python-RabbitMQ


[RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-one-python)

[Pika Doc for RabbitMQ configuration](https://pika.readthedocs.io/en/stable/index.html)


# Installation
## Create the `.env` file

Set `RABBITMQ_USER`, `RABBITMQ_PASSWORD` value in the `.env` file.

## Run the RabbitMQ(docker-compose)

    docker compose up -d

Go to the [RabbitMQ Localhost Dashboard](http://127.0.0.1:15672/) after the build is complete. login using the `RABBITMQ_USER`, `RABBITMQ_PASSWORD` values.


## Python script

1. Publisher
`publisher.py` is publishing a message to the queue `hello_queue`.

2. Receiver
`receive.py` receives messages from the queue `hello_queue`.
