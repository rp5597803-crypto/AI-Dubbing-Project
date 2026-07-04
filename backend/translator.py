from deep_translator import GoogleTranslator


def translate_text(text, source="auto", target="en"):
    """
    Translate text using Google Translator.
    """

    if not text.strip():
        return ""

    translated = GoogleTranslator(
        source=source,
        target=target
    ).translate(text)

    return translated


def translate_segments(segments, source="auto", target="en"):
    """
    Translate Whisper timestamp segments.
    """

    translated_segments = []

    for segment in segments:

        translated_text = GoogleTranslator(
            source=source,
            target=target
        ).translate(segment["text"])

        translated_segments.append({
            "id": segment["id"],
            "start": segment["start"],
            "end": segment["end"],
            "text": translated_text
        })

    return translated_segments


if __name__ == "__main__":

    sample = "नमस्ते, आप कैसे हैं?"

    print(
        translate_text(
            sample,
            source="hi",
            target="en"
        )
    )
