import os
from openai import OpenAI
import json



def llm_rewrite_query(text: str) -> dict:
    """
    Returns:
    {
        "query": "...",
        "keywords": ["..."],
        "intent": "product|store|category|unknown"
    }
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {
            "query": text,
            "keywords": [],
            "intent": "unknown"
        }
    client = OpenAI(api_key=api_key)
    prompt = f"""
        Return ONLY valid JSON (no text) with the following structure:
        {{
        "query": string,
        "keywords": string[],
        "intent": "product" | "store" | "category" | "unknown"
        }}

        User request:
        {text}
        """

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    try:
        return json.loads(resp.output_text)
    except Exception:
        return {
            "query": text,
            "keywords": [],
            "intent": "unknown"
        }
