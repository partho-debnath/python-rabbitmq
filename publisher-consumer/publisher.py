import os, sys, json, time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rabbit_connection import get_rabbitmq_connection


def publish_message():

    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()
        queue_name = "hello_queue"
        channel.queue_declare(queue=queue_name)
        for i in range(1, 10):
            # message = {f"key_{i}": f"value {i}"}
            message = i
            channel.basic_publish(
                exchange="",
                routing_key=queue_name,
                body=json.dumps(message),
            )
            print(f"Published =>'{message}'<= message.")
            time.sleep(1)
        channel.close()
    except Exception as e:
        print("Error", e)


publish_message()
