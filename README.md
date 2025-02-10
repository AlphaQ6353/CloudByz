# **Loading and Using the Model**

## **Introduction**
This README provides instructions to load and inspect a trained TensorFlow/ Keras model stored in best_model_custom.keras file.

## **Requirements**
Ensure you have the following dependencies installed:

```pip install tensorflow```

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

## **Notes**

- Ensure best_model_custom.keras is present in the same directory as your script.

- If you encounter an error, ensure you have installed TensorFlow correctly.

## **Future Improvements**

- Add inference code for making predictions using the model.

- Integrate model evaluation with test data.

