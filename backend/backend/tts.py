from gtts import gTTS
import os


def text_to_speech(text, output_file, language="en"):
    """
    Convert text to speech using gTTS.
    """

    if not text.strip():
        raise ValueError("Text is empty.")

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    tts = gTTS(
        text=text,
        lang=language,
        slow=False
    )

    tts.save(output_file)

    return output_file


def text_list_to_audio(text_list, output_folder, language="en"):
    """
    Convert multiple text segments into audio files.
    """

    os.makedirs(output_folder, exist_ok=True)

    audio_files = []

    for index, text in enumerate(text_list):

        filename = os.path.join(
            output_folder,
            f"segment_{index + 1}.mp3"
        )

        text_to_speech(
            text,
            filename,
            language
        )

        audio_files.append(filename)

    return audio_files


if __name__ == "__main__":

    sample = "Hello, welcome to AI Video Dubbing."

    text_to_speech(
        sample,
        "output/sample.mp3",
        "en"
    )

    print("Speech generated successfully.")
