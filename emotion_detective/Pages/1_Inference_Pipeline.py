import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

# Function to load Lottie animations from local JSON files
def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Set page configuration
st.set_page_config(
    page_title="Emotion Detective",
    page_icon="😊",
    layout="wide",  # Wide layout for better spacing
    initial_sidebar_state="expanded",  # Expanded sidebar by default
)

# Custom CSS for the app1``
custom_css = """
    <style>
    body {
        background-color: #2c2c2c;  /* Dark background */
        color: #f0f0f0;  /* Light text */
    }
    .sidebar .sidebar-content {
        background-color: #ffcc00;  /* Dark yellow sidebar */
        color: #2c2c2c;  /* Dark text */
    }
    .sidebar .sidebar-content h2 {
        color: #2c2c2c;  /* Dark text for the sidebar title */
    }
    .css-18e3th9 {
        padding-top: 3.5rem;  /* Adjust top padding to avoid overlap */
    }
    .css-1v3fvcr {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #2c2c2c;  /* Dark text */
    }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Add a title
st.title("Emotion Detective")

# Subtitle
st.markdown("## 🔍 Inference Pipeline")

import streamlit as st
import requests
import json
import pandas as pd

# Function to send the POST request
def send_request(model_type, media_file):
    # Determine model path and emotion mapping based on model type
    if model_type == "roberta":
        model_path = "./models/roberta.pth"
        emotion_mapping_path = "./models/mapping_emotions_roberta.json"
    else:
        model_path = "./models/rnn.pth"
        emotion_mapping_path = "./models/mapping_emotions_rnn.json"
    
    # Determine input media path based on selected file
    input_media_path = f"./data/{media_file}"
    
    # Prepare the payload
    payload = json.dumps({
        "input_media_path": input_media_path,
        "model_path": model_path,
        "model_type": model_type,
        "emotion_mapping_path": emotion_mapping_path
    })
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    # Send the request
    url = "http://194.171.191.226:3950/inference"
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # Parse the response
    return response.json()

# Dropdown for model type
model_type = st.selectbox("Select Model", ("roberta", "rnn"))

# Dropdown for media file
media_file = st.selectbox("Select Media File", ("EmotionsforKids.mp3", "EmotionsforKids.mp4"))

# Button to trigger the request
if st.button("Send Request"):
    response_data = send_request(model_type, media_file)
    
    # Convert response JSON to DataFrame and display
    df = pd.DataFrame(response_data)
    st.dataframe(df)

# Add a styled footer with horizontal line
st.markdown("""
    <hr>
    <p style='text-align: center; color: #666; font-size: 14px;'>
    &copy; 2024 Emotion Detective | NLP Group-1
    </p>
""", unsafe_allow_html=True)
