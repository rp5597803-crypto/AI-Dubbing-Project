const uploadBtn = document.getElementById("uploadBtn");
const videoFile = document.getElementById("videoFile");
const language = document.getElementById("language");
const statusBox = document.getElementById("status");
const resultBox = document.getElementById("result");

uploadBtn.addEventListener("click", async () => {

    if (videoFile.files.length === 0) {
        alert("Please select a video.");
        return;
    }

    const formData = new FormData();
    formData.append("video", videoFile.files[0]);
    formData.append("language", language.value);

    statusBox.innerHTML = "⏳ Uploading video...";
    resultBox.innerHTML = "";

    try {

        const response = await fetch(
            "http://localhost:5000/upload",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        if (data.success) {

            statusBox.innerHTML =
                "✅ AI dubbing completed successfully.";

            resultBox.innerHTML = `
                <h3>Completed</h3>

                <p><b>File:</b> ${data.filename}</p>

                <p><b>Translated Text:</b></p>

                <textarea
                    rows="8"
                    style="width:100%;margin-top:10px;"
                    readonly>${data.translated_text}</textarea>

                <br><br>

                <a
                    class="download-btn"
                    href="http://localhost:5000${data.download}"
                    target="_blank">
                    Download Dubbed Video
                </a>
            `;

        } else {

            statusBox.innerHTML =
                "❌ Processing failed.";

        }

    } catch (error) {

        console.error(error);

        statusBox.innerHTML =
            "❌ Cannot connect to backend.";

    }

});
