import streamlit as st
import os

st.set_page_config(page_title="Subtitle Remover", layout="centered")

st.title("🎬 Subtitle Remover App")
st.write("Upload a video file and this app will show it back to you (demo).")

uploaded_file = st.file_uploader("Upload your video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.success("Video uploaded successfully!")
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.read())

    st.video("temp_video.mp4")
    st.info("Note: This is a placeholder. Actual subtitle removal coming soon.")
