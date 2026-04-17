from infrastructure.logger import get_logger
logger = get_logger(__name__)

class Screenworker():
    def __init__(self,kafka_consumer,ads_repo,s3_client,redis_client):
        self.kafka_consumer = kafka_consumer
        self.ads_repo = ads_repo
        self.s3_client = s3_client
        self.redis_client = redis_client

    def run(self):
        for message in self.kafka_consumer:
            try:
                if message.value['event'] == "COUPON_CLAIMED":
                    store_id = message.value['store_id']
                    
                    try:
                        cached = self.redis_client.get(f"screen:current_ad:{store_id}")
                        if cached:
                            continue
                        
                        result = self.ads_repo.get_ad_by_store_id(store_id)
                        asset_url = result[3]
                        s3_url = self.s3_client.generate_presigned_url(asset_url)
                        self.redis_client.set("screen:current_ad", s3_url)
                        
                    except Exception:
                        logger.warning("Redis unavailable, falling back to DB")
                        result = self.ads_repo.get_ad_by_store_id(store_id)
                        asset_url = result[3]
                        s3_url = self.s3_client.generate_presigned_url(asset_url)
                        
            except Exception as e:
                logger.error(f"Screenworker.run failed: {e}")
                continue