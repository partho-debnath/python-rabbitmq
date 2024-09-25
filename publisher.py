import os
import pika
from dotenv import load_dotenv

load_dotenv()

credentials = pika.credentials.PlainCredentials(
    os.getenv("RABBITMQ_USER"),
    os.getenv("RABBITMQ_PASSWORD"),
)
try:
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host="127.0.0.1",
            port="5672",
            credentials=credentials,
            heartbeat=60,
        ),
    )
    channel = connection.channel()
    queue_name = "hello_queue"
    channel.queue_declare(queue=queue_name)
    channel.basic_publish(exchange="", routing_key=queue_name, body="Hello World-2!")
    channel.close()
    print(" [x] Sent 'Hello World!'")
except Exception as e:
    print("Error", e)
