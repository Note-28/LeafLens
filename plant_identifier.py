import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the pre-trained model (replace the path with your model file path)
model = load_model('Model/xception_model.keras')  # Adjust path to the saved model

# Function to preprocess the image before prediction
def preprocess_image(image):
    image = cv2.resize(image, (299, 299))  # Resize for Xception model
    image = image / 255.0  # Normalize the image to [0,1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to predict the class of the leaf in the image
def predict_image(image, model):
    img_array = preprocess_image(image)  # Preprocess the image
    predictions = model.predict(img_array)  # Make prediction
    score = tf.nn.sigmoid(predictions[0])  # Use sigmoid for multi-label classification
    predicted_class = np.argmax(score)  # Get the index of the highest score
    confidence = 100 * np.max(score)  # Get the confidence score
    return predicted_class, confidence

# Initialize the camera feed
cap = cv2.VideoCapture(0)  # 0 to use the default camera

while True:
    ret, frame = cap.read()  # Read the frame from the camera
    
    if not ret:
        print("Failed to grab frame")
        break
    
    # Show the current frame on the screen
    cv2.imshow('Camera Feed - Press c to Capture, q to Quit', frame)

    # Wait for key press and capture on 'c'
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('c'):  # Capture the frame on 'c' key press
        predicted_class, confidence = predict_image(frame, model)  # Predict the class
        print(f"Prediction Class {predicted_class} with {confidence:.2f}% confidence.")
        
        # Display prediction on the frame
        cv2.putText(frame, f'Class {predicted_class} ({confidence:.2f}%)', (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Show the frame with the prediction
        cv2.imshow('Prediction', frame)

    elif key == ord('q'):  # Quit the program on 'q' key press
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
