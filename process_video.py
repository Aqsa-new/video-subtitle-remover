import subprocess
import os

def process_video(input_path, output_path):
    temp_frames_dir = "temp/frames"
    os.makedirs(temp_frames_dir, exist_ok=True)

    # Extract frames
    subprocess.run([
        "ffmpeg", "-i", input_path,
        os.path.join(temp_frames_dir, "frame_%04d.png")
    ])

    # (Mock) "remove subtitles": just reuse the same frames
    # AI inpainting would go here later

    # Rebuild video
    subprocess.run([
        "ffmpeg", "-framerate", "24", "-i", os.path.join(temp_frames_dir, "frame_%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", output_path
    ])
