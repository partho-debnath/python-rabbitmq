import os, sys, json, time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rabbit_connection import get_rabbitmq_connection


def publish_message():

    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()
        channel.exchange_declare(
            exchange='logs',
            exchange_type='fanout',
        )
        for i in range(1, 501):
            message = i
            channel.basic_publish(
                exchange="logs",
                routing_key='',
                body=json.dumps(message),
            )
            print(f"Published Logs =>'{message}'<= message.")
            time.sleep(0.5)
        channel.close()
    except Exception as e:
        print("Error", e)


publish_message()
