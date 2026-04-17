from kafka import KafkaProducer,KafkaConsumer
import json

class MallKafkaProducer():
    def __init__(self,bootstrap_servers):
        
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def publish(self, topic, message):
        self.producer.send(topic, message)

class MallKafkaConsumer():
    def __init__(self,topic, bootstrap_servers):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=bootstrap_servers,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )
    
    def __iter__(self):
        return iter(self.consumer)