import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

# Set the page configuration
st.set_page_config(
    page_title="Emotion Detective - Training Pipeline",
    page_icon="🚀",
    layout="wide",
)

# Custom CSS for a quirky and playful look
st.markdown("""
    <style>
    body {
        background-color: #eef1f5; /* Light grey-blue background */
        color: #333333; /* Dark grey text */
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
    }
    .title {
        text-align: center;
        font-size: 3.5rem;
        margin-bottom: 1rem;
        color: #FF5722; /* Orange color for title */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Soft shadow */
        animation: fadeIn 1s ease-in-out; /* Fade-in animation */
    }
    .subtitle {
        text-align: center;
        font-size: 2rem;
        margin-bottom: 1.5rem;
        color: #5e5e5e; /* Grey subtitle */
        animation: fadeIn 1s ease-in-out; /* Fade-in animation */
    }
    .file-uploader {
        text-align: center;
        margin-bottom: 2rem;
        animation: slideIn 1s ease-in-out; /* Slide-in animation */
    }
    .file-upload-btn {
        background-color: #FF5722; /* Orange button */
        color: #ffffff; /* White text */
        font-weight: bold;
        padding: 0.8rem 1.5rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .file-upload-btn:hover {
        background-color: #FF7043; /* Darker shade on hover */
    }
    .file-upload-btn:disabled {
        background-color: #b3b3b3; /* Light grey when disabled */
        cursor: not-allowed;
    }
    .file-info {
        text-align: center;
        margin-top: 1.5rem;
        animation: slideIn 1s ease-in-out; /* Slide-in animation */
    }
    .dataframe {
        background-color: #ffffff; /* White background for dataframes */
        color: #333333; /* Dark text color */
        border-color: #FF5722; /* Orange border */
    }
    .footer {
        text-align: center;
        color: #777777; /* Light grey footer text */
        margin-top: 3rem;
        font-size: 0.9rem;
        animation: fadeIn 1s ease-in-out; /* Fade-in animation */
    }
    .footer a {
        color: #FF5722; /* Orange link color */
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .highlight {
        background-color: #FFECB3; /* Light yellow background */
        padding: 0.2rem 0.5rem;
        border-radius: 3px;
        font-weight: bold;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    @keyframes slideIn {
        from {
            transform: translateY(-20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    </style>
""", unsafe_allow_html=True)


# Title for training page
st.markdown("<h1 class='title'>🚀 Emotion Detective - Training Pipeline 🌟</h1>", unsafe_allow_html=True)

import streamlit as st
import requests
import json

# Function to send the POST request for training
def send_training_request(train_data_path, model_type, num_epochs, learning_rate, train_batch_size, eval_batch_size):
    payload = {
        "train_data_path": train_data_path,
        "test_data_path": "./data/CSV/5000_sampled_emotions_validation.csv",
        "text_column": "text",
        "emotion_column": "label",
        "num_epochs": num_epochs,
        "model_type": model_type,
        "model_dir": "./models",
        "model_name": f"{model_type}_test_api",
        "learning_rate": learning_rate,
        "train_batch_size": train_batch_size,
        "eval_batch_size": eval_batch_size,
        "cloud_logging": False
    }

    headers = {
        'Content-Type': 'application/json'
    }

    url = "http://194.171.191.226:3950/train"
    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

    return response.json()

st.markdown("<h2 class='subtitle'>📚 Training Configuration</h2>", unsafe_allow_html=True)

# Dropdown for model type
model_type = st.selectbox("Select Model Type", ("rnn", "roberta"))

# Dropdown for training data path
train_data_path = st.selectbox("Select Training Data Path", 
                               ("./data/CSV/5000_sampled_emotions_training.csv", "./data/CSV/train_set_5000.csv"))

# Slider for number of epochs
num_epochs = st.slider("Number of Epochs", min_value=1, max_value=100, value=1)

# Slider for learning rate
learning_rate = st.slider("Learning Rate", min_value=0.0001, max_value=0.1, value=0.001, step=0.0001)

# Slider for training batch size
train_batch_size = st.slider("Training Batch Size", min_value=1, max_value=128, value=4)

# Slider for evaluation batch size
eval_batch_size = st.slider("Evaluation Batch Size", min_value=1, max_value=128, value=8)

# Button to trigger the training request
if st.button("Start Training"):
    response_data = send_training_request(train_data_path, model_type, num_epochs, learning_rate, train_batch_size, eval_batch_size)
    
    # Display the response
    st.json(response_data)


# Add a footer
st.markdown("""
    <hr>
    <p class='footer'>
    &copy; 2024 Emotion Detective | NLP Group-1
    </p>
""", unsafe_allow_html=True)
