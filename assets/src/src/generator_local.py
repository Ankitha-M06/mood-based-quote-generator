# src/generator_local.py
import random

TEMPLATES = {
    "positive": [
        "You're doing amazing — keep going and celebrate every small win!",
        "Keep riding this wave of good energy; your progress matters."
    ],
    "neutral": [
        "Small steps forward count — take one today and be kind to yourself.",
        "A calm moment and a single action can turn a day around."
    ],
    "negative": [
        "It's okay to feel this way. One small step now is a victory — you are stronger than you think.",
        "Tough times pass. Be gentle with yourself and take one tiny step forward."
    ]
}

def generate_quote_local(mood: str, user_context: str = "") -> str:
    options = TEMPLATES.get(mood, TEMPLATES["neutral"])
    quote = random.choice(options)
    if user_context:
        quote += f" ({user_context})"
    return quote

if __name__ == "__main__":
    print(generate_quote_local("negative", "exam tomorrow"))
