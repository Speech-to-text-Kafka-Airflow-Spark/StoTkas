from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging

# from datetime import datetime
# from json import dumps
# from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:9092')
future = producer.send('cart-topic',b'banana')


# while True:
#     timestampStr = datetime.now().strftime("%H:%M:%S")
#     print("Sending: " + timestampStr)
#     producer.send('timestamp', timestampStr)
#     sleep(5)
