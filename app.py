import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

IMAGE_SIZE = 256

CLASS_NAMES = [
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___Healthy"
]

model = tf.keras.models.load_model("Potato_Disease_Model.keras")

st.title("Potato Disease Classification")
st.write("Upload a potato leaf image and the model will predict the disease.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((IMAGE_SIZE, IMAGE_SIZE))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = round(100 * np.max(prediction[0]), 2)

    st.subheader("Prediction")
    st.write(f"Class: **{predicted_class}**")
    st.write(f"Confidence: **{confidence}%**")
