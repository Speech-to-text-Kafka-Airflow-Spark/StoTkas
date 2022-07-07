from ensurepip import bootstrap
from http import client
from kafka import KafkaAdminClient
from kafka.admin import NewTopic

client = KafkaAdminClient(
    bootstrap_servers=['localhost:9092'],
    client_id='admin-client'
)
topic_list = []
topic_list.append(NewTopic(name='cart-topic', num_partitions=1, replication_factor=1))
client.create_topics(new_topics=topic_list, validate_only=False)
