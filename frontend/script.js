document.getElementById("generateBtn").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value;
    const num = document.getElementById("numSentences").value;
    const outputDiv = document.getElementById("output");

    if (!text.trim()) {
        outputDiv.innerHTML = "⚠ Please paste textbook content first.";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/generate-notes", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text,
                num_sentences: Number(num)
            })
        });

        const data = await response.json();
        outputDiv.style.whiteSpace = "pre-wrap";
        outputDiv.innerHTML = "📝 <b>Generated Notes:</b>\n\n" + data.notes;

    } catch (error) {
        outputDiv.innerHTML = "❌ Error connecting to backend server. Please make sure FastAPI is running.";
    }
});

