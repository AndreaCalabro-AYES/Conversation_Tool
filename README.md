# Conversation_Tool

## Overview
The **Conversation_Tool** is designed to enable a basic voice interaction with anyone in front of the screen. It is implementing NLP for sentiment analysis, will contain TTS and STT algorithms, and soon a custom model (based on TinyGPT) to have conversation on topics linked to hobbies and work.
Right now, on windows, you can just run the container service linked to the sentiment analysis using
   ```bash
   docker-compose run combined_analysis
   ```
To add the connection to the microphone and speakers would require too much overhead, and now is not a priority.

## Key Features
- **Real-Time Conversation Management:** Monitor and manage conversations in real-time.
- **Analysis Tools:** Built-in analytics for evaluating dialogue flow and participant engagement.
- **Extensibility:** Easily integrates with other systems for enhanced functionality.

## Setup Instructions

### Prerequisites
- Ensure you have Docker Desktop correctly setup

### Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AndreaCalabro-AYES/Conversation_Tool.git
    ```
    