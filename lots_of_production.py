from connection import pikachannel
import time
with pikachannel() as channel:
    for i in range(4,50):
        channel.basic_publish('muslih','python-q',f'This is the {i} numbered message 4-50')
        time.sleep(1)