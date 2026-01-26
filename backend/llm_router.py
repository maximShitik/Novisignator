import os
from openai import OpenAI
import json



def llm_pick_best_query(text: str, terms: list[str]) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {"queries": [text], "intent": "unknown", "reason": "missing_api_key"}

    client = OpenAI(api_key=api_key)

    terms_block = ""
    if terms:
        terms_block = "\nKnown DB terms (examples):\n" + "\n".join(terms[:50])

    prompt = f"""
You are a semantic router for a mall navigation system.

Return ONLY valid JSON with this exact structure:
{{
  "queries": string[],
  "intent": "product" | "store" | "category" | "unknown",
  "reason": string
}}

Rules:
- Hebrew only.
- Queries must be short noun phrases suitable for SQL LIKE.
- Provide 3–5 alternative queries.

User request:
{text}
{terms_block}
"""

    resp = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    try:
        return json.loads(resp.output_text)
    except Exception:
        return {"queries": [text], "intent": "unknown", "reason": "bad_json"}
