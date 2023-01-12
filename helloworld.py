from connection import pikachannel

with pikachannel() as channel:

    channel.basic_publish(exchange='muslih',
                        routing_key='python-q',
                        body='Hello World!')
    print(" [x] Sent 'Hello World!'")
