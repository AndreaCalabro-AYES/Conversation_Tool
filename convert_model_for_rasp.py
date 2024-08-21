import os
import torch
import onnx
from transformers import MobileBertForSequenceClassification
from onnx import checker, shape_inference
from onnxsim import simplify
import onnx2tf
import tensorflow as tf

print("Starting the conversion process...", flush=True)

# Environment variables
model_dir = os.environ.get("MODEL_DIR", "/app/pytorch_models")
onnx_dir = os.environ.get("ONNX_DIR", "/app/onnx_models")
tflite_dir = os.environ.get("TFLITE_DIR", "/app/tflite_models")

# Define paths
onnx_model_path = os.path.join(onnx_dir, "mobilebert.onnx")
simplified_onnx_model_path = os.path.join(onnx_dir, "mobilebert_simplified.onnx")
tf_saved_model_path = os.path.join(onnx_dir, "mobilebert_saved_model")
tflite_model_path = os.path.join(tflite_dir, "mobilebert.tflite")
quantized_tflite_model_path = os.path.join(tflite_dir, "mobilebert_quantized.tflite")

# Step 1: Load the PyTorch model and convert to ONNX
model = MobileBertForSequenceClassification.from_pretrained(model_dir)
model.eval()
dummy_input = torch.randint(0, 30522, (1, 128), dtype=torch.long)
torch.onnx.export(model, dummy_input, onnx_model_path, opset_version=11)
print("Step 1: Model converted to ONNX format.", flush=True)

# Step 2: Simplify the ONNX model
print("Simplifying the ONNX model...", flush=True)
onnx_model = onnx.load(onnx_model_path)
simplified_model, check = simplify(onnx_model)
assert check, "Simplified ONNX model could not be validated"
onnx.save(simplified_model, simplified_onnx_model_path)
print("Step 2: ONNX model simplified.", flush=True)

# Step 3: Convert ONNX model to TensorFlow SavedModel using onnx2tf

print("Converting ONNX model to TensorFlow SavedModel using onnx2tf...", flush=True)
onnx2tf.convert(simplified_onnx_model_path, output_folder_path=tf_saved_model_path)
print(f"Step 3: ONNX model converted to TensorFlow SavedModel format at {tf_saved_model_path}.")
# Check if the SavedModel was successfully created
if os.path.exists(tf_saved_model_path):
    print(f"Step 3: ONNX model converted to TensorFlow SavedModel format at {tf_saved_model_path}.", flush=True)
    print(f"Contents of {tf_saved_model_path}:")
    print(os.listdir(tf_saved_model_path))
else:
    print(f"Error: SavedModel not found at {tf_saved_model_path}. Conversion might have failed.", flush=True)
    exit(1)

# Step 4: Convert TensorFlow SavedModel to TensorFlow Lite
print("Converting TensorFlow model to TensorFlow Lite format...", flush=True)
converter = tf.lite.TFLiteConverter.from_saved_model(tf_saved_model_path)
tflite_model = converter.convert()

with open(tflite_model_path, "wb") as f:
    f.write(tflite_model)
print("Step 4: Model converted to TensorFlow Lite format.", flush=True)

# Step 5: Optimize the TensorFlow Lite model using quantization
print("Optimizing TensorFlow Lite model using quantization...", flush=True)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_tflite_model = converter.convert()

with open(quantized_tflite_model_path, "wb") as f:
    f.write(quantized_tflite_model)
print("Step 5: Model optimized and saved as quantized TensorFlow Lite format.", flush=True)
