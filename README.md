# LeafLens

Dive into the world of botany with **LeafLens**. Armed with the power of the Xception model, this project transforms your device into a leaf-identifying superhero. Just point your camera, and let LeafLens unveil the mysteries of nature one leaf at a time! Whether you're a curious nature lover or a budding botanist, LeafLens is here to help you discover the leafy wonders around you. 🌿🔍

## Abstract

This project focuses on developing an automated system for identifying various species of leaves using the Xception model, a deep learning architecture known for its efficiency in image classification tasks. The model is trained on a diverse dataset of plant leaves to enhance accuracy and reliability.

## Introduction

With the increasing interest in plant biodiversity, the need for automated identification systems has become paramount. This project aims to leverage advanced machine learning techniques to accurately classify plant leaves based on image data.

## Project Overview

- **Objective**: To create a robust system capable of identifying and classifying leaf species from images.
- **Dataset**: The dataset comprises images of 83 different leaf species, totaling over 7,000 images.
- **Model Architecture**: The Xception model is utilized due to its superior performance in handling image data through depthwise separable convolutions.

## Dataset Description

- The dataset consists of images sourced from various botanical collections.
- Each class corresponds to a specific leaf species, facilitating supervised learning.

## Usage

### Using the Camera for Leaf Identification

The LeafLens project allows users to identify leaves in real-time using their device's camera. Follow these steps to get started:

1. **Setup**:
   - Ensure you have a working camera on your device (internal or external).
   - Make sure the required libraries (`opencv-python`, `tensorflow`, and `numpy`) are installed. You can install them using:
     ```bash
     pip install opencv-python tensorflow numpy
     ```

2. **Run the Camera Script**:
   - Navigate to the directory containing the `plant_identifier.py` script. 
   - Use the provided Bash script to run the program. Open your terminal and execute:
     ```bash
     ./scripts/firewall_automation.sh
     ```
     (Ensure the script is executable by running `chmod +x scripts/firewall_automation.sh` if necessary.)

3. **Capture Leaf Images**:
   - Once the camera feed is active, a window displaying the live camera feed will open.
   - **Press 'c'** to capture an image of the leaf you want to identify. The model will process the image and display the predicted class and confidence score on the screen.

4. **View Prediction**:
   - After capturing, the prediction will be displayed on the captured frame, showing the class of the leaf and the confidence percentage.

5. **Exit the Program**:
   - To exit the camera feed, **press 'q'**. This will close the camera window and terminate the program.

### Important Notes:
- Ensure the lighting conditions are good for better accuracy in predictions.
- The model's predictions depend on the training dataset; therefore, it may not recognize all leaf species accurately.

### Example Usage

```bash
# Run the camera identification script
./Scripts/firewall_automation.sh
```

## Conclusion
Saving the model and its weights allows for efficient use of the trained model in future applications. By following the methods outlined in this section, you can ensure that your model is preserved and easily retrievable for later use, whether for inference or continued training.

We will integrate this model with a camera module to enable real-time identification of leaves, enhancing its practical applications in biodiversity research and education.

## Contributing

Feel free to open issues or submit pull requests for any improvements. Contributions are welcome!

## Author

- Manan Punatu
