import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
import logging
from google.colab import drive

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Mount Google Drive
logger.info("Mounting Google Drive...")
drive.mount('/content/drive', force_remount=True)

# Load the tokenizer and model
logger.info("Loading tokenizer and model...")
tokenizer = AutoTokenizer.from_pretrained('google/mobilebert-uncased')
model = TFAutoModelForSequenceClassification.from_pretrained('google/mobilebert-uncased', num_labels=2)

# Load the dataset
logger.info("Loading dataset...")
data = pd.read_csv('merged_dataset.csv')  # Replace with your dataset path

# Preprocess the dataset
logger.info("Preprocessing dataset...")
label_map = {'negative': 0, 'positive': 1}
data['label'] = data['sentiment'].map(label_map)
data = data.dropna(subset=['label'])
data['label'] = data['label'].astype(int)

# Split the dataset
logger.info("Splitting dataset into train and validation sets...")
train_texts, val_texts, train_labels, val_labels = train_test_split(data['text'], data['label'], test_size=0.23, random_state=42)

# Tokenization and Filtering
logger.info("Tokenizing and filtering texts...")
max_length = 128

filtered_train_texts = []
filtered_train_labels = []
for text, label in zip(train_texts, train_labels):
    if len(tokenizer.tokenize(text)) <= max_length:
        filtered_train_texts.append(text)
        filtered_train_labels.append(label)

filtered_val_texts = []
filtered_val_labels = []
for text, label in zip(val_texts, val_labels):
    if len(tokenizer.tokenize(text)) <= max_length:
        filtered_val_texts.append(text)
        filtered_val_labels.append(label)

filtered_train_labels = pd.Series(filtered_train_labels)
filtered_val_labels = pd.Series(filtered_val_labels)

train_encodings = tokenizer(filtered_train_texts, truncation=True, padding='max_length', max_length=max_length, return_tensors="tf")
val_encodings = tokenizer(filtered_val_texts, truncation=True, padding='max_length', max_length=max_length, return_tensors="tf")

# Create TensorFlow datasets
logger.info("Creating TensorFlow datasets...")
train_dataset = tf.data.Dataset.from_tensor_slices((dict(train_encodings), filtered_train_labels)).batch(24)
val_dataset = tf.data.Dataset.from_tensor_slices((dict(val_encodings), filtered_val_labels)).batch(24)

# Compile the model
logger.info("Compiling the model...")
optimizer = tf.keras.optimizers.Adam(learning_rate=5e-5)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metrics = [tf.keras.metrics.SparseCategoricalAccuracy('accuracy')]

model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

# Train the model with early stopping
logger.info("Starting model training...")
callbacks = [
    tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3, verbose=1),
    tf.keras.callbacks.ModelCheckpoint('/content/drive/MyDrive/model_results/mobilebert_model', save_best_only=True, monitor='val_loss', mode='min', save_format='tf')
]

history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=3,
    callbacks=callbacks
)

# Evaluate the model
logger.info("Evaluating the model...")
val_loss, val_accuracy = model.evaluate(val_dataset)
logger.info(f"Validation loss: {val_loss}, Validation accuracy: {val_accuracy}")

# Save the model to Google Drive
logger.info("Saving the model and tokenizer...")
model_dir = '/content/drive/MyDrive/model_results/mobilebert_tf_model'
model.save_pretrained(model_dir)
tokenizer.save_pretrained(model_dir)
logger.info(f"Model and tokenizer saved at {model_dir}")
