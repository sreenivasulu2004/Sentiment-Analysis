import streamlit as st
import time
from SentimentAnalyser import SentimentAnalyser

def analyze_sentiment(text):
    """
    Placeholder function for sentiment analysis.
    Replace this with your actual sentiment analysis model/API call.

    Args:
        text (str): Input text to analyze

    Returns:
        dict: Dictionary containing sentiment and confidence
    """
    # Simulate processing time
    time.sleep(0.5)

    sentiment_analyser = SentimentAnalyser(
        vectorizer_path="Models/tfidf_vectorizer.pkl",
        encoder_path="Models/label_encoder.pkl",
        model_path="Models/classifier.pkl"
    )

    return sentiment_analyser.predict_sentiment(text)


def get_sentiment_color(sentiment):
    """Return color based on sentiment"""
    colors = {
        "Positive": "#4CAF50",  # Green
        "Negative": "#F44336",  # Red
        "Neutral": "#FF9800"  # Orange
    }
    return colors.get(sentiment, "#757575")


def main():
    # Page configuration
    st.set_page_config(
        page_title="Sentiment Analyzer",
        page_icon="🎭",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        color: #2E3440;
        font-size: 2.5rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .sub-header {
        text-align: center;
        color: #5E81AC;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }

    .sentiment-result {
        text-align: center;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border: 2px solid;
    }

    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #E5E9F0;
        font-size: 16px;
    }

    .stButton button {
        background: linear-gradient(45deg, #5E81AC, #88C0D0);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(94, 129, 172, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown('<h1 class="main-header">🎭 Sentiment Analyzer</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Discover the emotion behind your text</p>', unsafe_allow_html=True)

    # Main container
    with st.container():
        # Text input
        user_input = st.text_area(
            "Enter your text here:",
            placeholder="Type something to analyze its sentiment...",
            height=120,
            key="text_input"
        )

        # Analyze button
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            analyze_button = st.button("✨ Analyze Sentiment", type="primary")

        # Analysis result
        if analyze_button and user_input.strip():
            with st.spinner("Analyzing sentiment..."):
                result = analyze_sentiment(user_input)

            sentiment = result
            color = get_sentiment_color(sentiment)

            # Display result
            st.markdown(f"""
            <div class="sentiment-result" style="border-color: {color}; background-color: {color}15;">
                <h2 style="color: {color}; margin: 0; font-size: 2rem;">
                    {sentiment}
                </h2>
            </div>
            """, unsafe_allow_html=True)

        elif analyze_button and not user_input.strip():
            st.warning("⚠️ Please enter some text to analyze!")

    # Footer
    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #8FBCBB; font-size: 0.9rem;'>"
        "Built with ❤️ using Streamlit"
        "</p>",
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
