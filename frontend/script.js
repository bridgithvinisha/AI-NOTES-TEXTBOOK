document.getElementById("generate-btn").addEventListener("click", async () => {
    const paragraph = document.getElementById("text-input").value.trim();
    const bullets = parseInt(document.getElementById("bullet-count").value);
    const resultDiv = document.getElementById("result");

    if (!paragraph) {
        resultDiv.innerHTML = "⚠ Please paste a textbook paragraph.";
        return;
    }

    resultDiv.innerHTML = "⏳ Generating notes... please wait...";

    try {
        const response = await fetch("https://ai-notes-textbook.onrender.com/generate-notes", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ paragraph, bullets })
        });

        if (!response.ok) {
            resultDiv.innerHTML = "⚠ Error generating notes. Try again.";
            return;
        }

        const data = await response.json();

        // Format notes into bullet list
        const formatted = data.notes
            .split("\n")
            .map(line => line.trim())
            .filter(line => line)
            .map(line => `• ${line}`)
            .join("<br>");

        resultDiv.innerHTML = formatted;

    } catch (error) {
        console.error(error);
        resultDiv.innerHTML = "🚨 Server unreachable. Please try again.";
    }
});


