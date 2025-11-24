# src/app.py
import streamlit as st
from src.sentiment import detect_mood
from src.generator_local import generate_quote_local

# try to import API generator (optional)
try:
    from src.generator_api import generate_quote_api
    api_available = True
except Exception:
    api_available = False

st.set_page_config(page_title="Mood-Based Quote Generator")
st.title("AI Mood-Based Quote Generator")
st.write("Type how you're feeling or paste a short sentence describing your mood/situation.")

user_input = st.text_area("How are you feeling?", height=120)

col1, col2 = st.columns(2)
with col1:
    use_api = st.checkbox("Use OpenAI (if API key configured)", value=False)
with col2:
    more_context = st.text_input("Optional: add a short context (e.g., 'exam stress')")

if st.button("Generate Quote"):
    if not user_input.strip():
        st.warning("Please type how you feel first.")
    else:
        mood = detect_mood(user_input)
        st.info(f"Detected mood: **{mood}**")
        if use_api and api_available:
            quote = generate_quote_api(mood, more_context)
        elif use_api and not api_available:
            st.error("OpenAI generator not configured. Falling back to local generator.")
            quote = generate_quote_local(mood, more_context)
        else:
            quote = generate_quote_local(mood, more_context)

        st.markdown("### Your Mood-Matched Quote")
        st.write(f"> {quote}")
        st.success("Share this! 💬")
