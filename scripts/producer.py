import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
import pandas as pd
from create_topic import Topics
class Producer:
    """ Create a producer and emit events from s3 bucket"""

    def __init__(self, bootstrap='b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092', create_topic=True, topic='transc_data'):
        self.bootstrap = bootstrap
        self.topic = topic
        self.create_topic = create_topic
  

    def start_publishing(self):
        """ Start producer by initializing producer"""
        self.get_data()
        self.initialize()
        if self.create_topic:
            tp = Topics('Benkart', [self.topic])
            tp.create_topics()
            self.topic = tp.topics[0]
        self.publish()

    def initialize(self):
        """ Initialize producer with bootstrap server """
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap,
            api_version=(0, 10, 1),
            value_serializer=lambda v: json.dumps(v).encode('UTF-8'),
            key_serializer=lambda v: json.dumps(v).encode('UTF-8')
        )