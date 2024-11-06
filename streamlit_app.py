# 2024.11.06 - Ben - Python | main

# Import necessary libraries
import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Set up the Streamlit app
st.title("IT Betyár - Braintumor Detection")

# Load the model
model = YOLO('best_tumor_detection_model_120.pt')

# Load the image
image_path = 'atomtest/out_test02_2.jpg'
img = Image.open(image_path)
st.image(img, caption="Input Image", width=400)

# Run the model on the image
results = model.predict(image_path)

# Display the annotated image
annotated_img = results[0].plot()  # YOLO plot() generates an image with bounding boxes
st.image(annotated_img, caption="Detection Results", use_column_width=True)

# Extract and display bounding box details
if results[0].boxes:
    box = results[0].boxes[0]  # Assuming only one box
    x_min, y_min, x_max, y_max = box.xyxy[0].tolist()  # Get bounding box coordinates
    confidence = box.conf[0].item()  # Confidence score
    class_name = results[0].names[int(box.cls[0].item())]  # Get the class name

    # Display bounding box details
    st.write(f"Bounding Box Coordinates: ({x_min:.2f}, {y_min:.2f}), ({x_max:.2f}, {y_max:.2f})")
    st.write(f"Confidence: {confidence:.2f}")
    st.write(f"Class Detected: {class_name}")
else:
    st.write("No detections found.")

