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

    statusBox.innerHTML = "Uploading video...";

    const formData = new FormData();
    formData.append("video", videoFile.files[0]);
    formData.append("language", language.value);

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
                "✅ Video uploaded successfully.";

            resultBox.innerHTML = `
                <p><b>File:</b> ${data.filename}</p>
                <p>AI dubbing pipeline will run in the next version.</p>
            `;

        } else {

            statusBox.innerHTML =
                "❌ Upload failed.";

        }

    } catch (error) {

        console.error(error);

        statusBox.innerHTML =
            "❌ Cannot connect to backend.";

    }

});
