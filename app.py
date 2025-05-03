# app.py

import streamlit as st
import grpc
import io
import protos.story2audio_pb2 as pb2
import protos.story2audio_pb2_grpc as pb2_grpc

# --- Page Configuration ---
st.set_page_config(
    page_title="🎙️ Story2Audio",
    page_icon="🎧",
    layout="centered"
)

# --- Header ---
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎙️ Story2Audio Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Turn your written stories into expressive audio using Kokoro TTS</p>", unsafe_allow_html=True)

# --- Input Section ---
st.markdown("### 📝 Enter your story")
text = st.text_area("", placeholder="Once upon a time in a land far, far away...")

# --- Button ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate = st.button("🔊 Generate Audio", use_container_width=True)

# --- gRPC Request ---
if generate and text.strip():
    with st.spinner("⏳ Generating audio... please wait"):
        try:
            # Connect to gRPC service
            channel = grpc.insecure_channel('localhost:50051')
            stub = pb2_grpc.Story2AudioServiceStub(channel)
            request = pb2.TextRequest(text=text)
            response = stub.GenerateAudio(request)

            if response.status == "success":
                st.markdown("### ✅ Your Audio")
                audio_bytes = io.BytesIO(response.audio_content)
                st.audio(audio_bytes, format='audio/wav')

                st.success("Audio generated successfully!")
            else:
                st.error("❌ Failed to generate audio. Please try again.")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
else:
    st.markdown("<small style='color: gray;'>Enter some text and click 'Generate Audio' to begin.</small>", unsafe_allow_html=True)
