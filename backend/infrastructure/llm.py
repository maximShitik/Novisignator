from openai import OpenAI
import json
from infrastructure.logger import get_logger
logger = get_logger(__name__)

class LLM():
    def __init__(self,api_key,model):
        self.llm_client = OpenAI(api_key=api_key)
        self.model = model

    def parse(self,message):
        try:
            response = self.llm_client.chat.completions.create(
                model=self.model,
                messages=[
                    { 
                        "role": "system", 
                        "content": """You are a mall assistant.
                                    Extract the intent and parameters from the user message.
                                    Always return store and product names in English, even if the user writes in Hebrew.
                                    Always respond ONLY with JSON in this format:
                                    {"intent": "find_store", "params": {"store_name": "Nike"}}
                                    Possible intents: find_store, find_product, navigate"""
                    },
                    { 
                        "role": "user", 
                        "content": message 
                    }
                ])
            text = response.choices[0].message.content
            return json.loads(text)
        except Exception as e:
            logger.error(f"LLMClient.parse failed: {e}")
            raise
