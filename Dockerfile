# Dockerfile
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install TextBlob, NLTK, and their dependencies
RUN pip install --no-cache-dir textblob nltk

# Download TextBlob corpora and NLTK VADER lexicon
RUN python -m textblob.download_corpora lite && \
    python -m nltk.downloader vader_lexicon

# Copy the sentiment analysis scripts into the container
COPY sentiment_analysis.py .
COPY test_textblob.py .
COPY test_vader.py .
COPY test_combined.py .

# Define the command to run the sentiment analysis script
# CMD ["python", "compare_models.py"]
