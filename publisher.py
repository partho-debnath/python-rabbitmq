from rabbit_connection import get_rabbitmq_connection


def publish_message():

    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()
        queue_name = "hello_queue"
        channel.queue_declare(queue=queue_name)
        message = "hello universe - 1"
        channel.basic_publish(exchange="", routing_key=queue_name, body=message)
        channel.close()
        print(f"Published '{message}' message.")
    except Exception as e:
        print("Error", e)


publish_message()
