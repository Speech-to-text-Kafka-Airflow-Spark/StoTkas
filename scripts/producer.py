from kafka import KafkaProducer
from kafka.errors import KafkaError

def createProducer():
    producer = KafkaProducer(bootstrap_servers=['b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092'])
    return producer