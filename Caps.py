from tensorflow.keras.models import load_model

model = load_model('best_model_custom.keras')
print("New Branched version")
model.summary()
