import json
import os

def save_transcription(json_file, transcription_data):
    """
    Save a new transcription entry to the JSON file.

    Args:
        json_file (str): Path to the JSON file.
        transcription_data (dict): New transcription data to append.
    """
    # Load existing data if the file exists, otherwise start with an empty list
    if os.path.exists(json_file):
        with open(json_file, "r", encoding="utf-8") as file:
            transcriptions = json.load(file)
    else:
        transcriptions = []

    # Append the new transcription data
    transcriptions.append(transcription_data)

    # Write the updated list back to the JSON file
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(transcriptions, file, indent=4, ensure_ascii=False)

    print(f"Transcription saved to {json_file}")
