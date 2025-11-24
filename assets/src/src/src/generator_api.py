# src/generator_api.py
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

if OPENAI_KEY:
    import openai
    openai.api_key = OPENAI_KEY

PROMPT_TEMPLATES = {
    "positive": "User is feeling positive. Write a short (1-2 sentence) uplifting motivational quote that matches a warm, celebratory tone. Make it personal and encouraging.",
    "neutral": "User is feeling neutral. Write a short (1-2 sentence) gentle motivational quote to uplift without being too emotional. Keep it simple and practical.",
    "negative": "User is feeling down/negative. Write a short (1-2 sentence) compassionate, supportive motivational message that acknowledges difficulty and offers hope."
}

def generate_quote_api(mood: str, user_context: str = "") -> str:
    if not OPENAI_KEY:
        return "OpenAI API key not configured. Please set OPENAI_API_KEY in a .env file."
    system_msg = "You are a helpful, empathetic assistant that crafts short motivational quotes."
    user_msg = PROMPT_TEMPLATES.get(mood, PROMPT_TEMPLATES["neutral"])
    if user_context:
        user_msg += f" Context: {user_context}"
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",   # replace with available model if needed
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        max_tokens=60,
        temperature=0.8,
        n=1
    )
    return resp['choices'][0]['message']['content'].strip()
