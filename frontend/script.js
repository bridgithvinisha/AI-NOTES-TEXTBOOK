document.getElementById("generateBtn").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value.trim();
    const bullets = document.getElementById("bulletCount").value;

    const outputDiv = document.getElementById("output");
    outputDiv.innerHTML = "⏳ Generating notes... please wait.";

    if (!text) {
        outputDiv.innerHTML = "⚠ Please enter some text.";
        return;
    }

    try {
        const response = await fetch(`/generate?text=${encodeURIComponent(text)}&bullets=${bullets}`);
        const data = await response.json();

        if (data.error) {
            outputDiv.innerHTML = `❌ Error: ${data.error}`;
        } else {
            outputDiv.innerHTML = `<ul>${data.notes
                .map((note) => `<li>${note}</li>`)
                .join("")}</ul>`;
        }
    } catch (err) {
        outputDiv.innerHTML = "🚨 Server unreachable. Please try again.";
        console.error(err);
    }
});


