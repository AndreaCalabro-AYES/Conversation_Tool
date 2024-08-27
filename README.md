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


   Error log
Step 4/8 : RUN pip install vosk
 ---> Running in 2a61492953e6
Collecting vosk
  Downloading vosk-0.3.45-py3-none-linux_armv7l.whl (2.4 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.4/2.4 MB 3.8 MB/s eta 0:00:00
Collecting cffi>=1.0
  Downloading cffi-1.17.0.tar.gz (516 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 516.1/516.1 kB 3.8 MB/s eta 0:00:00
  Installing build dependencies: started
  Installing build dependencies: finished with status 'done'
  Getting requirements to build wheel: started
  Getting requirements to build wheel: finished with status 'done'
  Preparing metadata (pyproject.toml): started
  Preparing metadata (pyproject.toml): finished with status 'done'
Collecting websockets
  Downloading websockets-13.0-py3-none-any.whl (142 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 143.0/143.0 kB 3.2 MB/s eta 0:00:00
Collecting requests
  Downloading requests-2.32.3-py3-none-any.whl (64 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 64.9/64.9 kB 2.4 MB/s eta 0:00:00
Collecting tqdm
  Downloading tqdm-4.66.5-py3-none-any.whl (78 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 78.4/78.4 kB 2.8 MB/s eta 0:00:00
Collecting srt
  Downloading srt-3.5.3.tar.gz (28 kB)
  Preparing metadata (setup.py): started
  Preparing metadata (setup.py): finished with status 'done'
Collecting pycparser
  Downloading pycparser-2.22-py3-none-any.whl (117 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 117.6/117.6 kB 3.3 MB/s eta 0:00:00
Collecting charset-normalizer<4,>=2
  Downloading charset_normalizer-3.3.2-py3-none-any.whl (48 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 48.5/48.5 kB 2.1 MB/s eta 0:00:00
Collecting certifi>=2017.4.17
  Downloading certifi-2024.7.4-py3-none-any.whl (162 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 163.0/163.0 kB 3.0 MB/s eta 0:00:00
Collecting idna<4,>=2.5
  Downloading idna-3.8-py3-none-any.whl (66 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 66.9/66.9 kB 2.9 MB/s eta 0:00:00
Collecting urllib3<3,>=1.21.1
  Downloading urllib3-2.2.2-py3-none-any.whl (121 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 121.4/121.4 kB 3.1 MB/s eta 0:00:00
Building wheels for collected packages: cffi, srt
  Building wheel for cffi (pyproject.toml): started
  Building wheel for cffi (pyproject.toml): finished with status 'error'
  error: subprocess-exited-with-error
  
  × Building wheel for cffi (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [48 lines of output]
      
          No working compiler found, or bogus compiler options passed to
          the compiler from Python's standard "distutils" module.  See
          the error messages above.  Likely, the problem is not related
          to CFFI but generic to the setup.py of any Python package that
          tries to compile C code.  (Hints: on OS/X 10.8, for errors about
          -mno-fused-madd see http://stackoverflow.com/questions/22313407/
          Otherwise, see https://wiki.python.org/moin/CompLangPython or
          the IRC channel #python on irc.libera.chat.)
      
          Trying to continue anyway.  If you are trying to install CFFI from
          a build done in a different context, you can ignore this warning.
      
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.linux-aarch64-cpython-39
      creating build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/pkgconfig.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/verifier.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/cparser.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/_shimmed_dist_utils.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/_imp_emulation.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/backend_ctypes.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/recompiler.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/lock.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/setuptools_ext.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/cffi_opcode.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/api.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/commontypes.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/ffiplatform.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/vengine_cpy.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/vengine_gen.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/__init__.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/model.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/error.py -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/_cffi_include.h -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/parse_c_type.h -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/_embedding.h -> build/lib.linux-aarch64-cpython-39/cffi
      copying src/cffi/_cffi_errors.h -> build/lib.linux-aarch64-cpython-39/cffi
      running build_ext
      building '_cffi_backend' extension
      creating build/temp.linux-aarch64-cpython-39
      creating build/temp.linux-aarch64-cpython-39/src
      creating build/temp.linux-aarch64-cpython-39/src/c
      gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O3 -Wall -fPIC -DFFI_BUILDING=1 -I/usr/include/ffi -I/usr/include/libffi -I/usr/local/include/python3.9 -c src/c/_cffi_backend.c -o build/temp.linux-aarch64-cpython-39/src/c/_cffi_backend.o
      error: command 'gcc' failed: No such file or directory
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for cffi
  Building wheel for srt (setup.py): started
  Building wheel for srt (setup.py): finished with status 'done'
  Created wheel for srt: filename=srt-3.5.3-py3-none-any.whl size=22446 sha256=65deb82f781b7b3494478b85f0fd4be33d9d526f6cbe41f10e8d674e8384a4c2
  Stored in directory: /root/.cache/pip/wheels/69/cb/6a/5e5977c5c1fab3b94ff429718103884855b0d5671ed9880100
Successfully built srt
Failed to build cffi
ERROR: Could not build wheels for cffi, which is required to install pyproject.toml-based projects

[notice] A new release of pip is available: 23.0.1 -> 24.2
[notice] To update, run: pip install --upgrade pip
The command '/bin/sh -c pip install vosk' returned a non-zero code: 1
ERROR: Service 'raspberry_chatbot' failed to build : Build failed

