import whisper

def transcribe_audio(audio_path, model_name="base"):
    """
    Transcribe audio using OpenAI's Whisper model.
    """
    print(f"Loading Whisper model: {model_name}")
    model = whisper.load_model(model_name)
    print(f"Transcribing audio: {audio_path}")
    transcription = model.transcribe(audio_path)
    return transcription['text']