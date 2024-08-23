from transformers import TFAutoModelForSequenceClassification
import tensorflow as tf

# Load the model using the correct method
model = TFAutoModelForSequenceClassification.from_pretrained('/app/tf_model')
print("Model loaded", flush=True)

# Convert to TensorFlow Lite with optimization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
print("Converter created", flush=True)

# Apply optimizations
converter.optimizations = [tf.lite.Optimize.DEFAULT]
print("Converter set for optimization", flush=True)

# You can further specify quantization if needed:
# This is post-training dynamic range quantization
# converter.target_spec.supported_types = [tf.float16]
# Save the optimized model

# Convert the model
tflite_model = converter.convert()
print("Model converted and optimized", flush=True)

with open('/app/tflite_model/mobilebert_model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Model optimization and conversion to TFLite complete.")