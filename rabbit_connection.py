import os
import pika
from dotenv import load_dotenv

load_dotenv()

credentials = pika.credentials.PlainCredentials(
    os.getenv("RABBITMQ_USER"),
    os.getenv("RABBITMQ_PASSWORD"),
)


def get_rabbitmq_connection():
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host="127.0.0.1",
                port="5672",
                credentials=credentials,
                heartbeat=60,
            ),
        )
        return connection
    except Exception as e:
        raise Exception(str(e))
