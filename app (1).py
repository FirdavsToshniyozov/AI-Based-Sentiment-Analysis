
import streamlit as st
from transformers import pipeline

st.title("AI-Powered Sentiment Analysis")
st.write("Analyze the sentiment of your text: Positive or Negative.")

user_input = st.text_area("Enter your text here:", "")

sentiment_pipeline = pipeline("sentiment-analysis")

if st.button("Analyze Sentiment"):
    if user_input.strip():
        result = sentiment_pipeline(user_input)
        sentiment = result[0]["label"]
        confidence = result[0]["score"]

        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Confidence Score:** {confidence:.2f}")
    else:
        st.warning("Please enter some text before analyzing!")
