import subprocess

def extract_audio(video_path, output_audio_path):
    """
    Extract audio from a video file using ffmpeg.
    """
    command = [
        "ffmpeg",
        "-i", video_path,               # Input video file
        "-q:a", "0",                    # Best audio quality
        "-map", "a",                    # Select audio stream
        output_audio_path,              # Output audio file
        "-y"                            # Overwrite output file
    ]
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Audio extracted to {output_audio_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting audio: {e.stderr.decode()}")