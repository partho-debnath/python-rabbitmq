import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rabbit_connection import get_rabbitmq_connection


def consumer():
    
    def callback(ch, method, properties, body):
        print("--------")
        # print("ch", ch)
        print("method", method)
        print("properties", properties)
        print("body", body)
        num = body.decode()
        print('num =>', num)
        ch.basic_ack(delivery_tag=method.delivery_tag)


    try:
        connection = get_rabbitmq_connection()
        channel = connection.channel()
        queue_name = "hello_queue"
        channel.queue_declare(queue=queue_name)
        channel.basic_consume(
            queue=queue_name,
            # auto_ack=True,
            on_message_callback=callback,
        )
        channel.start_consuming()

    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: ", e)
        sys.exit(0)
    except Exception as e:
        print("Error", e)


consumer()
