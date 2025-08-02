---
share: true
hidden: false
excalidraw-plugin: 
excalidraw-open-md: false
tags:
  - project
title: 
status: DONE
priority: medium
start: 2025-02-20
due: 2025-06-20
completion: 2025-02-20
---

This page walks you through how to generate audio files from PDFs using qpdf, pdfminer, and MeloTTS.

Input: .pdf | .txt
Output: .wav, .txt

## Environment

**Install and enable Windows Subsystem for Linux (WSL) on windows.** Skip this step if you already have a linux environment set up.

Win + X > Windows PowerShell > Enter the following
`wsl --install`

> [!caution]
> You may have to enable CPU Virtualization in BIOS for WSL to function.

**Install a distro to WSL.** I use OpenSUSE Tumbleweed. You can do the same by going to Microsoft Store and installing OpenSUSE Tumbleweed.

Create this file or append the following line to **allocate more memory to WSL**:

`C:\Users\USERNAME\.wslconfig`

```
[wsl2]
memory=16GB # Adjust based on your system
processors=4
```

**Start WSL**

```bash
wsl
```

Once the WSL is started, I use VSCode with the extension `WSL` to access files and CLI easily.

```bash
code .
```

As an alternative to bash, you can also use VSCode with the command (F1 Key) `Connect to WSL`, then enter the same command in the terminal.

## Dependencies

### System Level

```
sudo zypper install git, qpdf
```

### Project Level

```
git clone https://github.com/myshell-ai/MeloTTS.git
```

**Create venv** within the MeloTTS Directory

```
cd MeloTTS
python3.11 -m venv venv
source venv/bin/activate
```

**Install Dependencies**

```
pip install pdfminer.six openai
```

**Install MeloTTS Dependencies**

```
cd MeloTTS
pip install -e .
pip install --upgrade pip
python -m unidic download
python -m nltk.downloader averaged_perceptron_tagger_eng
```

## Run Script

**Create the folder** `files` under `MeloTTS` and copy your PDF/TXT file there.

**Rename the PDF/TXT** properly.

Set **OpenAI API Key**.

	Linux macOS
	`export OPENAI_API_KEY='your_api_key_here'`
	
	Windows
	`set OPENAI_API_KEY=your_api_key_here`

**Review settings** before running the script with `python pdf2wav.py`

`pdf2wav.py`

```python
import os
import subprocess
import shutil
import torch
import openai
from melo.api import TTS

# User Configurable Options
LANGUAGE = input("Language (EN, FR, ES, ZH, JP, KR) (default 'EN'): ") or 'EN'
ACCENT = input("Accent (EN-US, EN-BR, EN-INDIA, EN-AU, EN-Default) (default 'EN-US'): ") or 'EN-US'
SPEED = float(input("Speed (default 1.0): ") or 1.0)
USE_EXISTING_TEXT = input("Use existing 'text.txt'? (y/n, default 'n'): ").lower() == 'y'
CLEAN_TEXT = input("Clean text using OpenAI API? (y/n, default 'n'): ").lower() == 'y'
PROCESS_START = int(input("Process Start Chunk Index (default 0): ") or 0)
PROCESS_END = int(input("Process End Chunk Index (-1 for all, default -1): ") or -1)
GENERATE_TTS = input("Generate TTS? (y/n, default 'y'): ").lower() != 'n'
GENERATE_LRC = input("Generate LRC? (y/n, default 'y'): ").lower() != 'n'

# Internal Settings
CHUNK_SIZE = {"default": 3000, "ZH": 3000, "EN": 15000}
openai.api_key = os.getenv("OPENAI_API_KEY")

# Device Check
if torch.cuda.is_available():
    device = 'cuda:0'
    print(f"CUDA is available. Using device: {torch.cuda.get_device_name(0)}")
else:
    device = 'cpu'
    print("CUDA is NOT available. Running on CPU.")

# 1. Set up paths
BASE_DIR = os.path.expanduser("./files")
file_bases = ["input", "decrypted", "text", "text_cleaned"]
file_paths = {name: os.path.join(BASE_DIR, f"{name}.pdf" if name in ["input", "decrypted"] else f"{name}.txt") for name in file_bases}

# Determine output base name
exclude_files = ["input.pdf", "decrypted.pdf", "text.txt"]
if USE_EXISTING_TEXT:
    text_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".txt") and f not in exclude_files]
    source_file = text_files[0] if text_files else "text.txt"
else:
    pdf_files = [f for f in os.listdir(BASE_DIR) if f.endswith(".pdf") and f not in exclude_files]
    if not pdf_files:
        print("No valid PDF file found to use as base name.")
        exit()
    source_file = pdf_files[0]

source_path = os.path.join(BASE_DIR, source_file)
output_base = os.path.join(BASE_DIR, os.path.splitext(source_file)[0])

if not USE_EXISTING_TEXT and source_file.endswith(".pdf"):
    shutil.copy2(source_path, file_paths["input"])
    print(f"📄 Selected PDF: {source_file} -> Renamed to 'input.pdf'")

    try:
        subprocess.run(["qpdf", "--decrypt", file_paths["input"], file_paths["decrypted"]], check=True)
        print("PDF Decrypted Successfully.")
    except subprocess.CalledProcessError:
        print("PDF Decryption Failed.")
        exit()

    try:
        subprocess.run(["pdf2txt.py", "-o", file_paths["text"], file_paths["decrypted"]], check=True)
        print("Text Extracted Successfully.")
    except subprocess.CalledProcessError:
        print("Text Extraction Failed.")
        exit()
else:
    shutil.copy2(source_path, file_paths["text"])

# 2. Clean Text using OpenAI API
if CLEAN_TEXT:
    with open(file_paths["text"], "r", encoding="utf-8") as f:
        raw_text = f.read()

    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a meticulous proofreader. Your task is to clean and correct text while preserving the original wording, structure, and meaning as much as possible. Only fix obvious OCR errors, spacing issues, and formatting inconsistencies. Do not paraphrase or rephrase."},
                {"role": "user", "content": f"Please clean and correct the following text while staying true to the original wording:\n{raw_text}"}
            ]
        )
        cleaned_text = response.choices[0].message.content


        with open(file_paths["text_cleaned"], "w", encoding="utf-8") as f:
            f.write(cleaned_text)
        print("Text cleaned and saved to 'text_cleaned.txt'.")
    except Exception as e:
        print(f"Text Cleaning Failed: {e}")
        exit()
else:
    shutil.copy2(file_paths["text"], file_paths["text_cleaned"])

# 3. Split Text into Chunks
with open(file_paths["text_cleaned"], "r", encoding="utf-8") as f:
    full_text = f.read()

chunk_size = CHUNK_SIZE.get(LANGUAGE, CHUNK_SIZE["default"])

def split_text_into_chunks(text, chunk_size):
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para = para.strip()
        if not para:
            continue

        non_empty_lines = [line for line in para.split('\n') if line.strip()]

        if len(current_chunk) + len(para) <= chunk_size or len(non_empty_lines) < 5:
            current_chunk += para + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

chunks = split_text_into_chunks(full_text, chunk_size=chunk_size)

# 4. Initialize MeloTTS
model = TTS(language=LANGUAGE, device=device)
speaker_ids = model.hps.data.spk2id

if not isinstance(speaker_ids, dict):
    speaker_ids = vars(speaker_ids)

# 5. Convert Each Chunk
start_idx = PROCESS_START
end_idx = PROCESS_END if PROCESS_END != -1 else len(chunks)

for idx in range(start_idx, end_idx):
    chunk = chunks[idx]
    output_wav = f"{output_base}_{idx:02d}.wav"
    output_lrc = f"{output_base}_{idx:02d}.txt"

    try:
        if GENERATE_TTS:
            speaker_id = speaker_ids.get(ACCENT, speaker_ids.get("EN-Default"))
            model.tts_to_file(chunk, speaker_id, output_wav, speed=SPEED)
            print(f"WAV File Created: {output_wav}")

        if GENERATE_LRC:
            with open(output_lrc, "w", encoding="utf-8", newline='') as lrc_file:
                for line in chunk.split('\n'):
                    if line.strip():
                        lrc_file.write(f"{line.strip()}\n")
            print(f"LRC File Created: {output_lrc}")

    except Exception as e:
        print(f"Processing Failed for Chunk {idx}: {e}")

print("Workflow Complete!")

```

*Created in collaboration with 4o.*

## Post Generation

I use foobar2000 to rename, convert to AAC and add metadata and replaygain.

For .txt lyrics files, I use this script to **batch rename**.

`batch_replace.py`

```python
import os

# Define replacements
replace_from = "The Birth of Tragedy_"
replace_to = ""

# Process files in the current directory
for filename in os.listdir():
    if filename.endswith(".txt") and replace_from in filename:
        new_name = filename.replace(replace_from, replace_to)
        os.rename(filename, new_name)
        print(f"Renamed: {filename} -> {new_name}")

print("✅ Renaming Complete.")
```

I then use [[../../2024/Plex_Media_Server/index|Plex Media Server]] to host them in my Library.
