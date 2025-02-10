# **Loading and Using the Model**

## **Introduction**
This README provides instructions to load and inspect a trained TensorFlow/ Keras model stored in best_model_custom.keras file.

## **Requirements**
Ensure you have the following dependencies installed:

```pip install tensorflow numpy```

## **Steps to Load and View Model Summary**

To load and check the summary of the model, use the following Python script:

```
from tensorflow.keras.models import load_model

model = load_model('best_model_custom.keras')
model.summary()
```

## **Running the Script**

Save the script as ```load_model.py``` and execute it using:

```python load_model.py```

This will display the structure of the loaded model.

## **Using the model for prediction**

To make predictions using the loaded model:

```
import numpy as np
import cv2
from tensorflow.keras.models import load_model

model = load_model("your_model.h5")

diseases = ['Healthy', 'Diabetic Retinopathy', 'Glaucoma', 'Cataract']

def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Resize to match model input size
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

image_path = input("Enter image path")
input_image = preprocess_image(image_path)

prediction = model.predict(input_image)
predicted_disease = diseases[np.argmax(prediction)]

print("Predicted Eye Condition:", predicted_disease)

```

## **Notes**

- Ensure best_model_custom.keras is present in the same directory as your script.

- If you encounter an error, ensure you have installed TensorFlow correctly.

- The input shape for predictions should match the model's expected input dimensions.

## **Future Improvements**

- Add inference code for making predictions using the model.

- Integrate model evaluation with test data.

- Develop a user-friendly API for model deployment.

