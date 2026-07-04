import os

from backend.ffmpeg_utils import (
    extract_audio,
    replace_audio
)

from backend.whisper_utils import (
    transcribe_audio
)

from backend.translator import (
    translate_text
)

from backend.tts import (
    text_to_speech
)


def process_video(
    video_path,
    target_language="en"
):
    """
    Complete AI dubbing pipeline.
    """

    os.makedirs("output", exist_ok=True)

    extracted_audio = "output/extracted_audio.wav"
    dubbed_audio = "output/dubbed_audio.mp3"
    final_video = "output/final_video.mp4"

    print("Step 1 : Extracting audio...")
    extract_audio(
        video_path,
        extracted_audio
    )

    print("Step 2 : Speech to Text...")
    result = transcribe_audio(
        extracted_audio
    )

    original_text = result["text"]

    print("Step 3 : Translating...")
    translated_text = translate_text(
        original_text,
        source="auto",
        target=target_language
    )

    print("Step 4 : Text to Speech...")
    text_to_speech(
        translated_text,
        dubbed_audio,
        language=target_language
    )

    print("Step 5 : Replacing audio...")
    replace_audio(
        video_path,
        dubbed_audio,
        final_video
    )

    return {
        "original_text": original_text,
        "translated_text": translated_text,
        "output_video": final_video
    }


if __name__ == "__main__":

    result = process_video(
        "uploads/sample.mp4",
        target_language="en"
    )

    print(result)
