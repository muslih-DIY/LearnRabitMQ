from connection import pikachannel

with pikachannel() as channel:

    channel.exchange_declare('muslih', durable=True, exchange_type='topic')
    channel.queue_declare(queue='muslih-python-q')
    channel.queue_bind(exchange='muslih', queue='muslih-python-q', routing_key='python-q')