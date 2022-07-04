const
    dropArea = document.querySelector(".drag-area"),
    dragText = dropArea.querySelector("header"),
    button = dropArea.querySelector("button"),
    input = dropArea.querySelector("input");
let file;

document.getElementById("get-file").onclick = () => {
    input.click()
}



input.addEventListener("change", function () {
    file = this.files[0];
    dropArea.classList.add("active");
    changeDetails()
});


dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("active");
    dragText.textContent = "Release to Upload File";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
});

dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    file = event.dataTransfer.files[0];
    changeDetails()
});

function changeDetails() {
    dragText.textContent = file.name

    var name = file.name
    if (name.slice(-5) == ".json") {
        document.getElementById("file-icon").src = "static/svg/json.svg"
    } else if (name.slice(-4) == ".pdf") {
        document.getElementById("file-icon").src = "static/svg/pdf.svg"

    } else if (name.slice(-4) == ".mp4" || name.slice(-4) == ".mkv") {
        document.getElementById("file-icon").src = "static/svg/video.svg"

    } else if ((name.slice(-4) == ".jpg") || (name.slice(-4) == ".png") || (name.slice(-4) == ".webp")) {
        document.getElementById("file-icon").src = "static/svg/image.svg"

    } else if (name.slice(-4) == ".vcf") {
        document.getElementById("file-icon").src = "static/svg/contacts.svg"
    } else {
        document.getElementById("file-icon").src = "static/svg/files.svg"
    }
    document.getElementById("upload-it").onchange = function () {
        document.getElementById("upload").submit();
        alert("Done")
    };
}