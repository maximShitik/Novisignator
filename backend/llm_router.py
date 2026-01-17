import os
from openai import OpenAI
import json

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def llm_rewrite_query(text: str) -> dict:
    """
    Returns:
    {
        "query": "...",
        "keywords": ["..."],
        "intent": "product|store|category|unknown"
    }
    """
    schema = {
        "type": "object",
        "properties": {
            "query": {"type": "string"},
            "keywords": {"type": "array", "items": {"type": "string"}},
            "intent": {"type": "string", "enum": ["product", "store", "category", "unknown"]},
        },
        "required": ["query", "keywords", "intent"],
        "additionalProperties": False
    }

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {"role": "system", "content": "You rewrite short shopping/navigation requests into a clean search query. Output only JSON that matches the schema."},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_schema", "json_schema": {"name": "rewriter", "schema": schema}},
    )

    # ב-Responses API הפלט נמצא ב-output_text ואז הוא JSON תקין בגלל הסכמה
    return json.loads(resp.output_text)
