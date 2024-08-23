import tflite_runtime.interpreter as tflite
import numpy as np
import re

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

# Initialize the TFLite interpreter
interpreter = tflite.Interpreter(model_path="mobilebert_model.tflite")
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Function to preprocess and tokenize input text
def preprocess_text(texts):
    return simple_tokenizer(texts)

def run_inference(text):
    # Preprocess the input
    preprocessed_input = preprocess_text([text])

    # Prepare input data as required by the model
    input_ids = preprocessed_input.astype(np.int32)
    attention_mask = np.ones((1, 128), dtype=np.int32)  # Attention mask with ones
    token_type_ids = np.zeros((1, 128), dtype=np.int32)  # Token type IDs with zeros

    # Set the tensors
    interpreter.set_tensor(input_details[0]['index'], attention_mask)
    interpreter.set_tensor(input_details[1]['index'], input_ids)
    interpreter.set_tensor(input_details[2]['index'], token_type_ids)

    # Run the inference
    interpreter.invoke()

    # Get the output tensor
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return output_data

def main():
    print("Model is ready for testing.")
    while True:
        user_input = input("Enter a sentence to analyze sentiment (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break

        predictions = run_inference(user_input)
        print(f"Predictions: {predictions}")

if __name__ == "__main__":
    main()
