# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Import libraries
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Set your API key from .env file
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load the correct vision model (supports image + text)
model = genai.GenerativeModel("gemini-2.5-pro")

# Function to get response from Gemini
def get_gemini_response(prompt, image):
    if prompt and image:
        response = model.generate_content([prompt, image])
    elif image:
        response = model.generate_content([image])
    elif prompt:
        response = model.generate_content(prompt)
    else:
        return "Please give a prompt or upload an image."
    return response.text

# Streamlit app starts here
st.set_page_config(page_title="Gemini Vision App")
st.header("🔍 Gemini Vision Q&A App")

# User input
prompt = st.text_input("Enter your prompt:")

# Image upload
uploaded_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Button to submit
if st.button("Generate"):
    with st.spinner("Generating response..."):
        result = get_gemini_response(prompt, image)
    st.subheader("🧠 Gemini Response:")
    st.write(result)
