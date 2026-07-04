import whisper
import os

# Load Whisper model only once
MODEL_NAME = "base"
model = whisper.load_model(MODEL_NAME)


def transcribe_audio(audio_path, language=None):
    """
    Convert speech to text using Whisper.
    """

    if not os.path.exists(audio_path):
        raise FileNotFoundError(audio_path)

    result = model.transcribe(
        audio_path,
        language=language,
        fp16=False
    )

    return {
        "text": result["text"],
        "language": result["language"],
        "segments": result["segments"]
    }


def save_transcript(text, output_file):
    """
    Save transcript to a text file.
    """

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(text)

    return output_file


def get_segments(audio_path):
    """
    Return Whisper timestamp segments.
    """

    result = model.transcribe(
        audio_path,
        fp16=False
    )

    return result["segments"]
