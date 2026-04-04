

class ChatService():
    def __init__(self, store_repo, product_repo, redis_client, llm_client):
        self.store_repo = store_repo
        self.product_repo = product_repo
        self.redis_client = redis_client
        self.llm_client = llm_client

    def handle_message(self,input): pass



    