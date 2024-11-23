import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from rabbit_connection import get_rabbitmq_connection


def subscribe_two():
    
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
        result = channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        
        channel.queue_bind(
            queue=queue_name,
            exchange='logs',
        )
        channel.basic_consume(
            queue=queue_name,
            on_message_callback=callback,
            # auto_ack=True,
        )
        channel.start_consuming()

    except KeyboardInterrupt as e:
        print("KeyboardInterrupt: ", e)
        sys.exit(0)
    except Exception as e:
        print("Error", e)


subscribe_two()
