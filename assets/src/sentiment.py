# src/sentiment.py
from textblob import TextBlob

def detect_mood(text: str) -> str:
    """
    Returns one of: 'positive', 'neutral', 'negative'
    """
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity  # -1.0 .. 1.0
    if polarity > 0.2:
        return "positive"
    elif polarity < -0.2:
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    sample = "I am very happy today!"
    print(detect_mood(sample))
