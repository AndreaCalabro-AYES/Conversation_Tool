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

Successfully built cb849c09f7b5
Successfully tagged conversation_tool_raspberry_chatbot:latest
Recreating raspberry_chatbot ... done
Attaching to raspberry_chatbot
raspberry_chatbot    | Traceback (most recent call last):
raspberry_chatbot    |   File "/app/converse.py", line 3, in <module>
raspberry_chatbot    |     import vosk
raspberry_chatbot    |   File "/usr/local/lib/python3.9/site-packages/vosk/__init__.py", line 36, in <module>
raspberry_chatbot    |     _c = open_dll()
raspberry_chatbot    |   File "/usr/local/lib/python3.9/site-packages/vosk/__init__.py", line 30, in open_dll
raspberry_chatbot    |     return _ffi.dlopen(os.path.join(dlldir, "libvosk.so"))
raspberry_chatbot    | OSError: cannot load library '/usr/local/lib/python3.9/site-packages/vosk/libvosk.so': /usr/local/lib/python3.9/site-packages/vosk/libvosk.so: cannot open shared object file: No such file or directory
raspberry_chatbot exited with code 1
