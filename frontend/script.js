const API_URL = "https://ai-notes-textbook.onrender.com/generate";

document.getElementById("generateBtn").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value.trim();
    const bullets = document.getElementById("bulletCount").value;
    const outputBox = document.getElementById("outputBox");

    if (!text) {
        outputBox.innerHTML = "⚠ Please enter some text.";
        return;
    }

    outputBox.innerHTML = "⏳ Generating notes... Please wait...";

    try {
        const response = await fetch(`${API_URL}?text=${encodeURIComponent(text)}&bullets=${bullets}`);
        const data = await response.json();

        if (data.notes) {
            outputBox.innerHTML = data.notes.replaceAll("•", "<br>•");
        } else {
            outputBox.innerHTML = "⚠ API Error: Could not generate notes.";
        }
    } catch (err) {
        outputBox.innerHTML = "🚨 Server unreachable. Try again later.";
    }
});




