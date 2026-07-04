import ffmpeg
import os


def extract_audio(video_path, output_audio):
    """
    Extract audio from a video file.
    """

    (
        ffmpeg
        .input(video_path)
        .output(
            output_audio,
            ac=1,
            ar=16000
        )
        .overwrite_output()
        .run()
    )

    return output_audio


def replace_audio(video_path, audio_path, output_video):
    """
    Replace original audio with dubbed audio.
    """

    video = ffmpeg.input(video_path)
    audio = ffmpeg.input(audio_path)

    (
        ffmpeg
        .output(
            video.video,
            audio.audio,
            output_video,
            vcodec="copy",
            acodec="aac",
            shortest=None
        )
        .overwrite_output()
        .run()
    )

    return output_video


def convert_to_wav(input_audio, output_wav):
    """
    Convert any audio format to WAV.
    """

    (
        ffmpeg
        .input(input_audio)
        .output(
            output_wav,
            ac=1,
            ar=16000
        )
        .overwrite_output()
        .run()
    )

    return output_wav
