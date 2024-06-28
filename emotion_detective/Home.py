import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Emotion Detective",
    page_icon="🕵️",
    layout="wide",
)

# Add custom CSS for dark mode styling and additional styles
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        color: #dcdcdc;
        font-family: 'Arial', sans-serif;
        padding: 2rem;
    }
    .title {
        text-align: center;
        font-size: 3.5rem;
        margin-bottom: 1rem;
        color: #66c2a5; /* Greenish color for title */
        text-shadow: 2px 2px 4px #000000; /* Shadow for title */
    }
    .subtitle {
        text-align: center;
        font-size: 1.8rem;
        margin-bottom: 2rem;
        color: #a9a9a9;
    }
    .overview {
        background-color: #333333; /* Darker background color */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2);
        margin-bottom: 2rem;
    }
    .overview-content {
        font-size: 1.3rem;
        line-height: 1.8;
        color: #dcdcdc;
        text-align: justify;
        font-style: italic;
    }
    .highlight {
        color: #66c2a5; /* Greenish color for highlight */
        font-weight: bold;
    }
    .gif-container {
        text-align: center;
        padding-top: 2rem;
        margin-top: 3rem;
        border-top: 1px solid #666666;
        border-bottom: 1px solid #666666;
        padding: 2rem 0;
    }
    .gif {
        width: 70%;
        max-width: 600px;
        height: auto;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.2); /* Box shadow for GIF */
        border-radius: 10px; /* Rounded corners for GIF */
    }
    .footer {
        text-align: center;
        color: #a9a9a9;
        margin-top: 3rem;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("<h1 class='title'>Emotion Detective 🕵️</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>NLP Project Overview</h2>", unsafe_allow_html=True)

# Overview section with enhanced and fancy styling
st.markdown("""
    <div class='overview'>
    <div class='overview-content'>
    <p style='font-size: 1.4rem;'><strong>This innovative NLP project</strong> harnesses the power of AI to detect emotions.</p>
    <p>Our tools provide <span class='highlight'>advanced capabilities</span> for emotion detection and analysis at a <em>sentence level</em>, enabling deep insights into emotional content.</p>
    <p>With dedicated pipelines for <span class='highlight'>model training</span> and <span class='highlight'>inference</span>, alongside comprehensive documentation, we deliver robust solutions for emotion intelligence.</p>
    </div>
    </div>
""", unsafe_allow_html=True)

# Display GIF with shadow and rounded corners
st.markdown("""
<div class='gif-container'>
    <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmQ3bGVoYWhrd3IwMTJ5Y3dtYmZzeWZ3MmVieG41Y2d2aGdjZzZpZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/42wQXwITfQbDGKqUP7/giphy.gif" alt="Detective GIF" class="gif">
</div>
""", unsafe_allow_html=True)

# Add a footer
st.markdown("""
    <p class='footer'>
    &copy; 2024 Emotion Detective | NLP Group-1
    </p>
""", unsafe_allow_html=True)
