from kafka import KafkaProducer
import json

class MallKafkaProducer():
    def __init__(self,bootstrap_servers):
        
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def publish(self, topic, message):
        self.producer.send(topic, message)
