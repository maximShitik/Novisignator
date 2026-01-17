import os
from openai import OpenAI
import json



def llm_pick_best_query(text: str, terms: list[str]) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key or not terms:
        return {"query": text, "keywords": [], "intent": "unknown"}

    client = OpenAI(api_key=api_key)

    prompt =  f"""
    You are a semantic router for a mall navigation system.

    The database may NOT contain the exact words the user typed.

    Your job is to understand the user's intent and suggest database search terms
    that could match RELATED products, categories, or store types.

    Return ONLY valid JSON with this exact structure:
    {{
    "queries": string[],
    "intent": "product" | "store" | "category" | "unknown",
    "reason": string
    }}

    Rules:
    - Do NOT repeat the user's text blindly.
    - If the user mentions an item that does not exist verbatim in the database,
    map it to a broader or related concept.
    - Prefer generic categories over specific brand names unless explicitly mentioned.
    - Queries must be short noun phrases suitable for SQL LIKE.
    - Provide 3–5 alternative queries.
    - Hebrew only.

    Examples:
    User: "נעלים"
    Good queries: ["הנעלה", "נעלי ספורט", "נעלי הליכה"]

    User: "משהו לאכול"
    Good queries: ["אוכל", "מסעדה", "קפה"]

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
