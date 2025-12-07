// Hosted API URL
const apiURL = "https://ai-notes-textbook.onrender.com/generate";

document.getElementById("generateBtn").addEventListener("click", async () => {
    const inputText = document.getElementById("inputText").value.trim();
    const bullets = Number(document.getElementById("bullets").value);
    const notesOutput = document.getElementById("notesOutput");

    if (!inputText) {
        notesOutput.innerHTML = "⚠️ Please paste some text first.";
        return;
    }

    notesOutput.innerHTML = "⏳ Generating notes, please wait...";

    try {
        const response = await fetch(apiURL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                text: inputText,
                bullets: bullets
            })
        });

        if (!response.ok) {
            notesOutput.innerHTML = "⚠️ Server unreachable or API error. Try again.";
            return;
        }

        const data = await response.json();
        if (!data.notes) {
            notesOutput.innerHTML = "⚠️ No notes generated. Try again.";
            return;
        }

        // Display notes with bullet formatting
        notesOutput.innerHTML = data.notes
            .replace(/\n/g, "<br>")
            .replace(/•/g, "✔️");

    } catch (error) {
        notesOutput.innerHTML = "🚨 Unable to connect to server. Please try again.";
        console.error(error);
    }
});



