from kafka.admin import KafkaAdminClient, NewTopic
class Topics():
    def __init__(self, group_name:str, topics:list)->None:
        '''Instatiate a class to create topic on aws. group_name is string, topics is a list of topics to be created'''
        self.group_name = group_name
        self.topics = [group_name +'_'+ topic for topic in topics]
        
    def create_topic(topic_name):
        admin_client = KafkaAdminClient(
        bootstrap_servers="localhost:9092", 
        client_id='group1'
    )

        topic_list = []
        topic_list.append(NewTopic(name="example_topic", num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)