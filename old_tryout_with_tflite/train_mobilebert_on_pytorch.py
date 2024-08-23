# GOOGLE COLLAB FILE TO BE USED TO TRAIN MOBILEBERT FOR SENTIMENT ANALYSIS


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from transformers import MobileBertTokenizer, MobileBertForSequenceClassification, AdamW, get_linear_schedule_with_warmup
import torch
from torch.utils.data import Dataset, DataLoader
from accelerate import Accelerator
from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Initialize Accelerator
accelerator = Accelerator()

# Load the tokenizer and model
tokenizer = MobileBertTokenizer.from_pretrained('google/mobilebert-uncased')
model = MobileBertForSequenceClassification.from_pretrained('google/mobilebert-uncased', num_labels=2)

# Load the dataset
data = pd.read_csv('merged_dataset.csv')  # Replace with your dataset path

# Preprocess the dataset
label_map = {'negative': 0, 'positive': 1}
data['label'] = data['sentiment'].map(label_map)
data = data.dropna(subset=['label'])
data['label'] = data['label'].astype(int)

# Split the dataset
train_texts, val_texts, train_labels, val_labels = train_test_split(data['text'], data['label'], test_size=0.23, random_state=42)

# Tokenization and Filtering
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

train_encodings = tokenizer(filtered_train_texts, truncation=True, padding='max_length', max_length=max_length)
val_encodings = tokenizer(filtered_val_texts, truncation=True, padding='max_length', max_length=max_length)

# Custom Dataset Class
class SentimentDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels.reset_index(drop=True)

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels.iloc[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = SentimentDataset(train_encodings, filtered_train_labels)
val_dataset = SentimentDataset(val_encodings, filtered_val_labels)

# Prepare DataLoader
batch_size = 12
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=batch_size)

# Prepare optimizer and learning rate scheduler
optimizer = AdamW(model.parameters(), lr=5e-5)
num_train_samples = len(filtered_train_texts)
num_train_batches = (num_train_samples + batch_size - 1) // batch_size
num_epochs = 3
num_training_steps = num_train_batches * num_epochs
scheduler = get_linear_schedule_with_warmup(optimizer, num_warmup_steps=500, num_training_steps=num_training_steps)

model, optimizer, train_loader, val_loader, scheduler = accelerator.prepare(
    model, optimizer, train_loader, val_loader, scheduler
)

# Training loop with early stopping and evaluation metrics
loss_threshold = 0.1
loss_window = []
stabilization_steps = 100

def find_avg(lst):
    return sum(lst)/len(lst)

model.train()
for epoch in range(num_epochs):
    print(f"Starting epoch {epoch+1}/{num_epochs}", flush=True)
    stop_epoch_early = False
    for step, batch in enumerate(train_loader):
        outputs = model(**batch)
        loss = outputs.loss
        accelerator.backward(loss)
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()

        loss_window.append(loss.item())
        if len(loss_window) > stabilization_steps:
            loss_window.pop(0)

        avg_recent_loss = find_avg(loss_window)
        if len(loss_window) == stabilization_steps and avg_recent_loss < loss_threshold:
            print(f"Stopping epoch {epoch+1} early at step {step+1}: average loss {avg_recent_loss} below threshold {loss_threshold}", flush=True)
            stop_epoch_early = True
            break

        if step % 100 == 0:
            print(f"Epoch {epoch+1}, Step {step}: loss = {loss.item()}", flush=True)

    if stop_epoch_early:
        print(f"Epoch {epoch+1} stopped early at step {step+1}", flush=True)

    # Evaluate the model after each epoch
    model.eval()
    val_preds = []
    val_labels_true = []
    for batch in val_loader:
        with torch.no_grad():
            outputs = model(**batch)
            logits = outputs.logits
            predictions = torch.argmax(logits, dim=-1)
            val_preds.extend(predictions.cpu().numpy())
            val_labels_true.extend(batch['labels'].cpu().numpy())

    accuracy = accuracy_score(val_labels_true, val_preds)
    f1 = f1_score(val_labels_true, val_preds, average='weighted')

    print(f"Epoch {epoch+1} completed - Accuracy: {accuracy:.4f}, F1-Score: {f1:.4f}", flush=True)
    model.train()

# Save the model
accelerator.wait_for_everyone()
unwrapped_model = accelerator.unwrap_model(model)

# Save the model to Google Drive
model_dir = '/content/drive/MyDrive/model_results'
unwrapped_model.save_pretrained(model_dir)
print("Model saved", flush=True)