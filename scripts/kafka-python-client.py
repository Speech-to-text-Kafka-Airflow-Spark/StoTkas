from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer, KafkaConsumer
from kafka import KafkaConsumer
from json import dumps, loads
import sys
import os
sys.path.insert(0, '../scripts/')
sys.path.insert(0, '../logs/')
sys.path.append(os.path.abspath(os.path.join('..')))
from log import App_Logger

app_logger = App_Logger("logs/kafka-python-client.log").get_app_logger()

class KafkaClient():
    def __init__(self, id: str, servers: list) -> None:
        try:
            self.kafka_servers = servers
            self.id = id
            self.consumer, self.producer, self.admin_client = None, None, None
            self.logger = App_Logger(
            "logs/kafka-python-client.log").get_app_logger()
            for index, server in enumerate(self.kafka_servers):
                print(f'\t{index + 1} - {server}')

        except Exception as e:
            self.logger.info(f"FAILED TO CREATE KafkaClient OBJECT INSTANCE")

    def create_admin_client(self) -> None:
        try:
            self.admin_client = KafkaAdminClient(
                    bootstrap_servers=self.kafka_servers,
                    client_id=self.id
                )
            self.logger.info('SUCCESSFULLY CREATED A KAFKA ADMIN CLIENT')

        except Exception as e:
            self.logger.info('FAILED TO CREATE A KAFKA ADMIN CLIENT')

    def get_topics(self) -> list:
        try:
            topics = self.admin_client.list_topics()

            self.logger.info('SUCCESSFULLY FETCHED KAFKA TOPICS')

            return topics

        except AttributeError:
            self.logger.info('INSTANTIATE A KAFKA ADMIN CLIENT FIRST USING THE create_admin_client METHOD')
        except Exception as e:
            self.logger.info("FAILED TO GET TOPICS")

    def create_topic_type(self, name: str, partitions: int = 1, replication_factor: int = 1) -> NewTopic:
        try:
            topic =  NewTopic(name=name, num_partitions=partitions, replication_factor=replication_factor)
            
            self.logger.info('SUCCESSFULLY INSTANTIATED A TOPIC OBJECT')

            return topic
        
        except Exception as e:
            self.logger.info("FAILED TO INSTANTIATE A TOPIC OBJECT")

    def create_topics(self, topics: list) -> None:
        try:
            result = self.admin_client.create_topics(new_topics=topics)

            self.logger.info(f"SUCCESSFULLY CREATED TOPICS:\nTOPICS CREATED:\n")
            for index, topic in enumerate(topics):
                print(f'\t{index} - {topic} - ADDED')
        except Exception as e:
            self.logger.info("FAILED TO CREATE TOPICS")

    def delete_topics(self, topic_names: list) -> None:
        try:
            self.admin_client.delete_topics(topics=topic_names)

            self.logger.info(f"SUCCESSFULLY DELETED TOPICS:\nTOPICS DELETED:\n")
            for index, topic in enumerate(topic_names):
                print(f'\t{index} - {topic} - DELETED')

        except Exception as e:
            self.logger.info("FAILED TO DELETE TOPICS")

    def create_producer(self, key_serializer=None, value_serializer=None, acks: int = 1, retries: int = 0, max_in_flight_requests_per_connection: int = 5):
        try:
            self.producer = KafkaProducer(
                client_id=self.id,
                bootstrap_servers=self.kafka_servers,
                key_serializer=key_serializer,
                value_serializer=value_serializer,
                acks=acks,
                retries=retries,
                max_in_flight_requests_per_connection=max_in_flight_requests_per_connection
            )

            self.logger.info(f"SUCCESSFULLY CREATED A KAFKA PRODUCER")
        except Exception as e:
            self.logger.info("FAILED TO CREATE A KAFKA PRODUCER")

    def send_data(self, topic_name: str, data_list: list, func=lambda x: x):
        try:
            for data in data_list:
                pass_data = func(data)
                self.producer.send(topic_name, value=pass_data)

            self.logger.info(f"SUCCESSFULLY SENT {len(data_list)} DATA VALUES")

        except AttributeError:
            self.logger.info('INSTANTIATE A KAFKA PRODUCER FIRST USING THE create_producer METHOD')

        except Exception as e:
            self.logger.info("FAILED TO SEND DATA")

    def create_consumer(self, topics: str, group_id: str, auto_commit: bool = True, offset: str = 'earliest', key_deserializer=None, value_deserializer=None, timeout: int = 20):
        try:
            self.consumer = KafkaConsumer(
                topics,
                client_id=self.id,
                bootstrap_servers=self.kafka_servers,
                auto_offset_reset=offset,
                enable_auto_commit=auto_commit,
                group_id=group_id,
                key_deserializer=key_deserializer,
                value_deserializer=value_deserializer,
                consumer_timeout_ms=timeout
            )

            self.logger.info(f"SUCCESSFULLY CREATED A KAFKA CONSUMER")

        except Exception as e:
            self.logger.info("FAILED TO CREATE A KAFKA CONSUMER")

    def get_data(self, verbose:int=0):
        try:
            return_data = []
            for message in self.consumer:
                message = message.value
                return_data.append(message)
                if(verbose == 1):
                    print(message)

            self.logger.info(f"SUCCESSFULLY FETCHED {len(return_data)} DATA VALUES")

            return return_data

        except AttributeError:
            self.logger.info('INSTANTIATE A KAFKA CONSUMER FIRST USING THE create_consumer METHOD')

        except Exception as e:
            self.logger.info("FAILED TO FETCH DATA")

    def get_json_serializer(self):
        return lambda x: dumps(x).encode('utf-8')

    def get_json_deserializer(self):
        return lambda x: loads(x.decode('utf-8'))


if __name__ == "__main__":

    kf_client = KafkaClient(
        'milkyb',
        [
            'b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092',
            'b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092'
        ]
    )

    kf_client.create_admin_client()

    print(kf_client.get_topics())

    kf_client.create_producer(
        value_serializer=kf_client.get_json_serializer())

    kf_client.create_consumer(
        topics='Reiten-Text-Corpus',
        offset='earliest',
        auto_commit=True,
        group_id='text-corpus-reader',
        value_deserializer=kf_client.get_json_deserializer())

    kf_client.send_data(topic_name='Reiten-Text-Corpus',
                        data_list=[{'number': 1}, {'number': 2}, {'number': 3}, {'number': 4}, {'number': 5}, {'number': 6}, {'number': 7}, {'number': 8}, {'number': 9}, {'number': 10}, {'number': 11}, {'number': 12}, {'number': 13}, {'number': 14}, {'number': 15}])

    print(kf_client.get_data())