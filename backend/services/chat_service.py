from infrastructure.logger import get_logger
logger = get_logger(__name__)


class ChatService():
    def __init__(self, store_repo, product_repo, redis_client, llm_client,navigation_service):
        self.store_repo = store_repo
        self.product_repo = product_repo
        self.navigation_service = navigation_service
        self.redis_client = redis_client
        self.llm_client = llm_client

    def handle_message(self,session_id,input):
        try:
            llm_response = self.llm_client.parse(input)

            intent = llm_response['intent']
            params = llm_response['params']

            cache_key = f"{intent}:{list(params.values())[0]}"
            scan_point_id = self.redis_client.get(f"session:{session_id}:scan_point")
            cached = self.redis_client.get(cache_key)
            if cached:
                return cached
            
            handlers = {
                        "find_store": lambda params: self.store_repo.get_by_name(params['store_name']),
                        "find_product": lambda params: self.product_repo.get_by_name(params['product_name']),
                        # "find_product_in_store": lambda params: self.product_repo.get_stores_by_product(params['product_id']),
                        "navigate": lambda params: self.navigation_service.get_route(scan_point_id, params['store_id'])}
            
            result = handlers[intent](params)

            self.redis_client.set(cache_key,result,ex=2592000)

            return result
        except Exception as e:
            logger.error(f"ChatService.handle_message failed: {e}")
            raise
        




    