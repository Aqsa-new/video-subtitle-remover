import streamlit as st
import os
import shutil

st.set_page_config(page_title="Subtitle Remover", layout="centered")

st.title("🎬 AI Video Subtitle Remover")
st.write("Upload a video with hardcoded subtitles, and this tool will process it (demo version).")

uploaded_file = st.file_uploader("📤 Upload your video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.success("✅ Video uploaded successfully!")
    
    # Save video to temp directory
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.read())
    
    st.video("temp_video.mp4")
    st.info("⚠️ In this demo version, subtitle removal is not active yet.")

    # Add download button for same file (just as a placeholder)
    with open("temp_video.mp4", "rb") as f:
        st.download_button("⬇️ Download processed video (same as uploaded)", f, file_name="processed_video.mp4")
