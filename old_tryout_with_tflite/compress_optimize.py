from transformers import TFAutoModelForSequenceClassification
import tensorflow as tf
import numpy as np

VOCABULARY_LEN = 30522

# # Load the model using the correct method
# model = TFAutoModelForSequenceClassification.from_pretrained('/app/tf_model')
# print("Model loaded", flush=True)

# # Ensure the input shape is set to [None, 128]
# input_spec = tf.TensorSpec([None, 128], tf.int32)
# model._set_inputs(input_spec, training=False)
# model.summary()

# Convert to TensorFlow Lite with optimization
converter = tf.lite.TFLiteConverter.from_saved_model('/app/tf_model')
print("Converter created", flush=True)

# Apply optimizations
converter.optimizations = [tf.lite.Optimize.DEFAULT]
print("Converter set for optimization", flush=True)

# Create a representative dataset generator function
def representative_data_gen():
    for _ in range(100):
        input_ids = np.random.randint(0, VOCABULARY_LEN, size=(1, 128)).astype(np.int32)
        attention_mask = np.ones((1, 128)).astype(np.int32)
        token_type_ids = np.zeros((1, 128)).astype(np.int32)
        yield [input_ids, attention_mask, token_type_ids]

# Set the representative dataset for quantization
converter.representative_dataset = representative_data_gen

# Convert the model
tflite_model = converter.convert()
print("Model converted", flush=True)
# Save the optimized model
with open('/app/tflite_model/mobilebert_model.tflite', 'wb') as f:
    f.write(tflite_model)

print("Model optimization and conversion to TFLite complete.")
