from connection import pikachannel
import time

def callback(ch,method,properties,body):
    print('Got a message from Queue A: ', body)

with pikachannel() as channel:
    channel.basic_consume(queue='muslih-python-q', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
    