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

---> Running in 401767f14d1e
Collecting pyinstaller
  Downloading pyinstaller-6.10.0.tar.gz (2.5 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.5/2.5 MB 3.7 MB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Requirement already satisfied: setuptools>=42.0.0 in /usr/local/lib/python3.9/site-packages (from pyinstaller) (58.1.0)
Collecting packaging>=22.0
  Downloading packaging-24.1-py3-none-any.whl (53 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 54.0/54.0 kB 2.2 MB/s eta 0:00:00
Collecting importlib-metadata>=4.6
  Downloading importlib_metadata-8.4.0-py3-none-any.whl (26 kB)
Collecting altgraph
  Downloading altgraph-0.17.4-py2.py3-none-any.whl (21 kB)
Collecting pyinstaller-hooks-contrib>=2024.8
  Downloading pyinstaller_hooks_contrib-2024.8-py3-none-any.whl (322 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 322.8/322.8 kB 3.4 MB/s eta 0:00:00
Collecting zipp>=0.5
  Downloading zipp-3.20.1-py3-none-any.whl (9.0 kB)
Building wheels for collected packages: pyinstaller
  Building wheel for pyinstaller (pyproject.toml): started
  Building wheel for pyinstaller (pyproject.toml): finished with status 'error'
  error: subprocess-exited-with-error
  
  × Building wheel for pyinstaller (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [21 lines of output]
      running bdist_wheel
      running build
      running build_bootloader
      No precompiled bootloader found or compile forced. Trying to compile the bootloader for you ...
      Setting top to                           : /tmp/pip-install-hu3_cjd9/pyinstaller_5fb211c4e33b43d0be6c791c1576f033/bootloader
      Setting out to                           : /tmp/pip-install-hu3_cjd9/pyinstaller_5fb211c4e33b43d0be6c791c1576f033/bootloader/build
      Python Version                           : 3.9.19 (main, Aug 13 2024, 21:53:03) [GCC 12.2.0]
      MSVC target(s)                           : not found
      Checking for 'gcc' (C compiler)          : /usr/bin/gcc
      Checking size of pointer                 : 4
      Platform                                 : Linux-32bit-arm detected based on compiler
      Checking for compiler flags -m32         : no
      Checking for linker flags -m32           : no
      Checking for compiler flags -Wno-error=unused-but-set-variable : yes
      Checking for library dl                                        : yes
      Checking for library pthread                                   : yes
      Checking for library m                                         : yes
      Checking for library z                                         : no
      The zlib development package is either missing or the shared library cannot be linked against. For security (and marginally better filesize), you should install the zlib-dev or zlib-devel packages with your system package manager, and try again. If you cannot do this (for example, distributions such as OpenWRT use sstrip on libraries, making linking impossible), then either use the --static-zlib option or set the PYI_STATIC_ZLIB=1 environment variable. If you are installing directly with pip, then use the environment variable.
      (complete log in /tmp/pip-install-hu3_cjd9/pyinstaller_5fb211c4e33b43d0be6c791c1576f033/bootloader/build/config.log)
      ERROR: Failed compiling the bootloader. Please compile manually and rerun setup.py
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pyinstaller
Failed to build pyinstaller
ERROR: Could not build wheels for pyinstaller, which is required to install pyproject.toml-based projects

[notice] A new release of pip is available: 23.0.1 -> 24.2
[notice] To update, run: pip install --upgrade pip
The command '/bin/sh -c pip install pyinstaller' returned a non-zero code: 1
ERROR: Service 'raspberry_chatbot' failed to build : Build failed
