# mood-based-quote-generator
AI Mood-Based Quote Generator (GenAI + Sentiment)


# Mood-Based Quote Generator

Generates short motivational quotes based on the user's mood. Mood detection uses TextBlob; generation uses either a simple local template engine or an LLM via OpenAI (optional).

## Files
- src/sentiment.py — detect mood (positive/neutral/negative)
- src/generator_local.py — template-based quote generator (no API needed)
- src/generator_api.py — OpenAI wrapper (optional)
- src/app.py — Streamlit UI

## Run (quick test in Google Colab)
We recommend running the demo in Google Colab (no installation). See instructions below.

## Notes
- Do NOT commit any `.env` or API keys.
- If using OpenAI, create a `.env` locally with `OPENAI_API_KEY=sk-...`
