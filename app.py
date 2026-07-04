from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER


@app.route("/")
def home():
    return jsonify({
        "project": "AI Video Dubbing",
        "status": "Running"
    })


@app.route("/upload", methods=["POST"])
def upload_video():

    if "video" not in request.files:
        return jsonify({"error": "No video selected"}), 400

    file = request.files["video"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    save_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(save_path)

    return jsonify({
        "success": True,
        "filename": file.filename,
        "path": save_path
    })


@app.route("/output/<filename>")
def download(filename):
    return send_from_directory(
        app.config["OUTPUT_FOLDER"],
        filename
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
