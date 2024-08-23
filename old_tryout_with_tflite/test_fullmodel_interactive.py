import tensorflow as tf
import numpy as np
import re

# Load the SavedModel
model_dir = '/app/tf_model'  # Update this path to your SavedModel directory
model = tf.saved_model.load(model_dir)
infer = model.signatures['serving_default']

# A simple tokenizer that replicates basic functionality
def simple_tokenizer(texts, vocab_size=30522, oov_token="<OOV>", max_length=128):
    word_index = {oov_token: 1}
    index = 2
    tokenized_texts = []

    for text in texts:
        tokens = re.findall(r'\b\w+\b', text.lower())
        tokenized_sequence = []
        for token in tokens:
            if token not in word_index:
                if len(word_index) < vocab_size:
                    word_index[token] = index
                    index += 1
            tokenized_sequence.append(word_index.get(token, word_index[oov_token]))

        # Pad or truncate to max_length
        if len(tokenized_sequence) > max_length:
            tokenized_sequence = tokenized_sequence[:max_length]
        else:
            tokenized_sequence.extend([0] * (max_length - len(tokenized_sequence)))

        tokenized_texts.append(tokenized_sequence)

    return np.array(tokenized_texts, dtype=np.int32)

def run_inference(text):
    # Preprocess the input
    preprocessed_input = simple_tokenizer([text])

    # Prepare input data as required by the model
    input_ids = preprocessed_input.astype(np.int32)
    attention_mask = np.ones((1, 128), dtype=np.int32)  # Attention mask with ones
    token_type_ids = np.zeros((1, 128), dtype=np.int32)  # Token type IDs with zeros

    # Create input tensor dictionary
    input_dict = {
        'input_ids': tf.convert_to_tensor(input_ids),
        'attention_mask': tf.convert_to_tensor(attention_mask),
        'token_type_ids': tf.convert_to_tensor(token_type_ids)
    }

    # Run the inference
    output = infer(**input_dict)
    return output['logits'].numpy()

def interpret_predictions(logits):
    # Apply softmax to convert logits to probabilities
    probabilities = tf.nn.softmax(logits, axis=-1).numpy()

    # Get the predicted class (the one with the highest probability)
    predicted_class = np.argmax(probabilities, axis=-1)[0]

    # Interpret the class
    class_names = ["negative", "positive"]
    predicted_label = class_names[predicted_class]

    return predicted_label, probabilities[0]

def main():
    print("Model is ready for testing.")
    while True:
        user_input = input("Enter a sentence to analyze sentiment (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        logits = run_inference(user_input)
        predicted_label, probabilities = interpret_predictions(logits)

        print(f"Predicted sentiment: {predicted_label}")
        print(f"Probabilities: {probabilities}")

if __name__ == "__main__":
    main()
