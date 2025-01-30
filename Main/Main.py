import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np

# Cache the model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('../Model/xception_model.keras')

model = load_model()
labels = [
    'Aloevera', 'Amla', 'Amruthaballi', 'Arali', 'Arjun Leaf', 'Astma_weed', 
    'Badipala', 'Balloon_Vine', 'Bamboo', 'Beans', 'Betel', 'Bhrami', 
    'Bringaraja', 'Caricature', 'Castor', 'Catharanthus', 'Chakte', 'Chilly', 
    'Citron lime (herelikai)', 'Coffee', 'Common rue(naagdalli)', 'Coriender', 
    'Curry', 'Doddpathre', 'Drumstick', 'Ekka', 'Eucalyptus', 'Ganigale', 
    'Ganike', 'Gasagase', 'Ginger', 'Globe Amarnath', 'Guava', 'Henna', 
    'Hibiscus', 'Honge', 'Insulin', 'Jackfruit', 'Jasmine', 'Kambajala', 
    'Kasambruga', 'Kohlrabi', 'Lantana', 'Lemon', 'Lemongrass', 'Malabar_Nut', 
    'Malabar_Spinach', 'Mango', 'Marigold', 'Marsh Pennywort Leaf', 'Mint', 
    'Neem', 'Nelavembu', 'Nerale', 'Nooni', 'Onion', 'Padri', 'Palak(Spinach)', 
    'Papaya', 'Parijatha', 'Pea', 'Pepper', 'Pomoegranate', 'Pumpkin', 
    'Raddish', 'Rose', 'Rubble Leaf', 'Sampige', 'Sapota', 'Seethaashoka', 
    'Seethapala', 'Spinach1', 'Tamarind', 'Taro', 'Tecoma', 'Thumbe', 
    'Tomato', 'Tulsi', 'Turmeric', 'ashoka', 'camphor', 'kamakasturi', 'kepala'
]

def is_leaf_image(image, model, threshold=0.64):
    img = tf.keras.preprocessing.image.load_img(image, target_size=(299, 299))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.sigmoid(predictions[0])
    confidence = np.max(score)

    return confidence >= threshold  # Returns True if leaf-like, else False

def predict_plant(image, model, labels, confidence_threshold=0.6):
    img = tf.keras.preprocessing.image.load_img(image, target_size=(299, 299))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.sigmoid(predictions[0])
    predicted_index = np.argmax(score)
    confidence = 100 * np.max(score)

    if confidence / 100 < confidence_threshold:
        return "Non-Leaf Image", confidence

    if predicted_index < len(labels):
        predicted_label = labels[predicted_index]
    else:
        predicted_label = "Unknown"

    return predicted_label, confidence

def get_plant_info(plant_name, file_path='../Information/plant_information.txt'):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
    
        plant_info = []
        is_plant = False

        for line in lines:
            if line.strip() == plant_name:
                is_plant = True
                plant_info.append(line)
            elif is_plant:
                if '~' in line:
                    break
                plant_info.append(line)
        
        if plant_info:
            return "\n".join(plant_info)
        else:
            return "No detailed information available for this plant."
    except FileNotFoundError:
        return "Plant information file not found."

# Streamlit App
st.title("Leaf Identification System 🌿")
st.subheader("Identify plants with high accuracy using Xception!")

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing the image..."):
        is_leaf = is_leaf_image(uploaded_file, model)

        if not is_leaf:
            st.warning("The uploaded image does not appear to be a leaf. Please upload a valid leaf image.")
        else:
            predicted_label, confidence = predict_plant(uploaded_file, model, labels)

            if predicted_label == "Non-Leaf Image":
                st.warning("The uploaded image does not appear to be a valid leaf image. Please upload a clearer image.")
            else:
                plant_info = get_plant_info(predicted_label)
                st.success(f"Prediction: {predicted_label}")
                st.info(f"Confidence: {confidence:.2f}%")
                st.markdown("### Plant Information:")
                st.write(plant_info)

                st.download_button(
                    label="Download Plant Information",
                    data=plant_info,
                    file_name=f"{predicted_label}_info.txt",
                    mime="text/plain",
                )
