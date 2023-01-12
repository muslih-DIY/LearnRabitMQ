#!/usr/bin/env python
import pika


class pikachannel:
    def __enter__(self):

        credentials = pika.PlainCredentials('magicQ','onlineQfortesting2022')
        # credentials = pika.PlainCredentials('muslih','muslihmagicQ2022')
        
        connection = pika.BlockingConnection(pika.ConnectionParameters('109.123.242.40',credentials=credentials))
        self.channel = connection.channel()
        return self.channel
    def __exit__(self,exc_type, exc_value, exc_tb):
        self.channel.close()

