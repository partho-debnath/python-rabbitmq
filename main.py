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
    print("-----")
    channel = connection.channel()
    print(channel is None)
    print("channel", channel)
except Exception as e:
    print("Error", e)
