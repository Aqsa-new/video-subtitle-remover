import streamlit as st
import os
import uuid
from process_video import process_video

st.title("🎬 Subtitle Remover (Demo)")

uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_file:
    file_id = str(uuid.uuid4())
    input_path = f"temp/{file_id}_input.mp4"
    output_path = f"temp/{file_id}_output.mp4"

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    st.video(input_path)
    st.write("Processing...")

    process_video(input_path, output_path)

    st.success("Subtitles removed! Download below:")
    st.video(output_path)
    with open(output_path, "rb") as f:
        st.download_button("📥 Download cleaned video", f, file_name="cleaned_video.mp4")
