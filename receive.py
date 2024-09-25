import sys
from rabbit_connection import get_rabbitmq_connection


def receive_message():

    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()
        queue_name = "hello_queue"
        channel.queue_declare(queue=queue_name)
        channel.basic_consume(
            queue=queue_name,
            auto_ack=True,
            on_message_callback=callback,
        )
        channel.start_consuming()

    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: ", e)
        sys.exit(0)
    except Exception as e:
        print("Error", e)


def callback(ch, method, properties, body):
    print("--------")
    print("ch", ch)
    print("method", method)
    print("properties", properties)
    print("body", body)


receive_message()
