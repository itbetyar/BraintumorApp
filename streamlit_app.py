# 2024.11.06 - Ben - Python | main

# Import necessary libraries
import streamlit as st
from PIL import Image

# Set up the Streamlit app
st.title("IT Betyár - Brain Tumor Detection")

# Add an image uploader to allow user to upload an image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Display the uploaded image if there is one
if uploaded_file is not None:
    # Load and display the uploaded image
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", width=400)
else:
    st.write("Please upload an image.")


