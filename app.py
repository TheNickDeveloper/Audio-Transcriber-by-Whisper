import streamlit as st
import tempfile
import os
import whisper

def main():
    st.set_page_config(page_title="Audio Transcriber", layout="centered")
    
    st.sidebar.header("⚙️ Settings")
    model_choice = st.sidebar.selectbox(
        "Select Whisper model",
        ["tiny","base","small"],
        index=0
    )

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
    return whisper.load_model(name)

if __name__ == "__main__":
    main()




