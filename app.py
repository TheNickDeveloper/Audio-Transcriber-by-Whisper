import streamlit as st
import torch
import whisper
import tempfile
import os

def main():
    st.set_page_config(page_title="Audio Transcriber", layout="centered")
    
    st.sidebar.header("⚙️ Settings")
    model_choice = st.sidebar.selectbox(
        "Select Whisper model",
        ["tiny"],
        index=0
    )

    torch_load_old = torch.load
    def torch_load_new(*args, **kwargs):
        if "weights_only" not in kwargs:
            kwargs["weights_only"] = False
        return torch_load_old(*args, **kwargs)

    torch.load = torch_load_new


    model = load_model(model_choice)
    st.title("🎙️ Audio Transcriber by Whisper")
    st.write("This is an applicatio that can help you to transcribe from audio to text and export to txt file. Please upload an audio file to get started.")
    uploaded_file = st.file_uploader("Upload Audio", type=["mp3", "wav", "m4a"])

    if uploaded_file is not None:
        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name

        st.audio(temp_path)

        if st.button("Transcribe"):
            with st.spinner(f"Transcribing using `{model_choice}` model..."):
                result = model.transcribe(temp_path)
                transcript = result["text"]

            st.subheader("Transcription:")
            st.write(transcript)

            st.download_button(
                label="🚀 Download Transcript",
                data=transcript,
                file_name="transcript.txt",
                mime="text/plain",
            )
            os.remove(temp_path)

@st.cache_resource
def load_model(name):
    local_model_path = f"./models/{name}.pt"
    return whisper.load_model(local_model_path)

if __name__ == "__main__":
    main()
