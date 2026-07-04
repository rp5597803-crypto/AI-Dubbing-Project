from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

from backend.replace_audio import process_video

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "project": "AI Video Dubbing Studio",
        "status": "Running"
    })


@app.route("/upload", methods=["POST"])
def upload():

    if "video" not in request.files:
        return jsonify({
            "success": False,
            "message": "No video selected."
        })

    video = request.files["video"]

    language = request.form.get(
        "language",
        "en"
    )

    video_path = os.path.join(
        UPLOAD_FOLDER,
        video.filename
    )

    video.save(video_path)

    result = process_video(
        video_path,
        target_language=language
    )

    return jsonify({
        "success": True,
        "filename": video.filename,
        "translated_text": result["translated_text"],
        "download":
            "/download/final_video.mp4"
    })


@app.route("/download/<filename>")
def download(filename):

    return send_from_directory(
        OUTPUT_FOLDER,
        filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
