import os
from video.extract_audio import extract_audio
from audio.transcribe import transcribe_audio
from persistance.save import save_transcription

def transcribe_video(video_path, json_file="transcriptions.json", model_name="base"):
    """
    Transcribe a video by extracting its audio and appending the transcription
    to a JSON file containing an array of transcriptions for other videos.

    Args:
        video_path (str): Path to the video file.
        json_file (str): Path to the JSON file where the transcription will be stored.
        model_name (str): Whisper model name to use for transcription.
    """
    audio_path = "temp_audio.mp3"  # Temporary file for extracted audio
    
    try:
        # Step 1: Extract audio from the video
        extract_audio(video_path, audio_path)
        
        # Step 2: Transcribe the audio
        transcription = transcribe_audio(audio_path, model_name=model_name)
        
        # Step 3: Prepare transcription data
        transcription_data = {
            "video_path": video_path,
            "transcription": transcription
        }
        
        # Step 4: Save transcription using the utility function
        save_transcription(json_file, transcription_data)
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Cleanup: Remove temporary audio file
        if os.path.exists(audio_path):
            os.remove(audio_path)
            print(f"Temporary file {audio_path} deleted.")

if __name__ == "__main__":
    # Example usage
    video_file = "sample.mp4"
    transcribe_video(video_file)
