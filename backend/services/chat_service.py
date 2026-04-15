

class ChatService():
    def __init__(self, store_repo, product_repo, redis_client, llm_client):
        self.store_repo = store_repo
        self.product_repo = product_repo
        self.redis_client = redis_client
        self.llm_client = llm_client

    def handle_message(self,input):
        handlers = {
    "find_store": lambda params: self.store_repo.get_by_name(params['store_name']),
    "find_product": lambda params: self.product_repo.get_by_name(params['product_name']),
    "claim_coupon": lambda params: self.coupon_service.claim_coupon(params['coupon_code']),
    "navigate": lambda params: self.navigation_service.navigate(params['store_id']),}
        
        



    