from repositories.ad_repository import AdRepository
from backend.workers.screenworker_service import Screenworker
from infrastructure.redis import create_redis_client
from infrastructure.s3 import MallS3
from infrastructure.kafka import MallKafkaConsumer
from infrastructure.db import create_db_pool
from backend.consts import DATABASE_URL,REDIS_HOST,REDIS_PORT,AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET, TOPIC,KAFKA_SERVERS


db_pool = create_db_pool(DATABASE_URL)
s3_client = MallS3(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET)
redis_client = create_redis_client(REDIS_HOST,REDIS_PORT)
kafka_consumer = MallKafkaConsumer(TOPIC, KAFKA_SERVERS)
ads_repo = AdRepository(db_pool)


if __name__ == '__main__':
    screenworker_service = Screenworker(kafka_consumer,ads_repo,s3_client,redis_client)
    screenworker_service.run()