# 🎙️ Audio Transcriber (Whisper + Streamlit)

A simple **web app** built with [Streamlit](https://streamlit.io/) and [OpenAI Whisper](https://github.com/openai/whisper) that transcribes audio files into text.  
You can upload an audio file (`.mp3`, `.wav`, `.m4a`) and get instant transcription, with the option to download the result as a `.txt` file.  

---
## 🌐 Live Demo

🔗 [Try it on Streamlit](https://audio-transcriber-by-whisper.streamlit.app/)

---

## 🪴 Application UIUX

![image](https://github.com/TheNickDeveloper/Audio-Transcriber-by-Whisper/blob/main/app_image.png)

---

## 🚀 Features
- Upload audio files (`mp3`, `wav`, `m4a`)
- Transcribe speech to text using Whisper
- View transcription directly in the browser
- Export the transcript as a `.txt` file
- Select different Whisper models (currently supports `tiny`)

---

## 🛠️ Installation

Clone this repo and install the required packages:

```bash
git clone https://github.com/yourusername/audio-transcriber.git
cd audio-transcriber
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Then open the link in your browser (usually http://localhost:8501).


## 📂 Project Structure

```bash
.
├── app.py              # Main Streamlit application
├── models/             # Folder for Whisper model files (e.g. tiny.pt)
├── requirements.txt    # Python dependencies
├── assets/             # Screenshots and demo GIFs
└── README.md           # Project documentation
```

## ⚙️ Model Weights

By default, the app looks for Whisper models in the ./models/ folder (e.g., models/tiny.pt).
You can download them directly from OpenAI Whisper releases or via:

```python
import whisper
model = whisper.load_model("tiny")
```
