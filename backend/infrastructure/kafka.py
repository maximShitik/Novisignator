from kafka import KafkaProducer

def create_kafka_producer(bootstrap_servers):
    return KafkaProducer(bootstrap_servers=bootstrap_servers)