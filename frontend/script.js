document.getElementById("generate-btn").addEventListener("click", async () => {
    const text = document.getElementById("input-text").value;
    const bulletCount = document.getElementById("bullet-count").value;

    if (!text.trim()) {
        alert("Please paste textbook content before generating notes.");
        return;
    }

    try {
        document.getElementById("output-notes").innerText = "⏳ Generating notes, please wait...";

        const response = await fetch("https://ai-notes-textbook.onrender.com/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                text: text,
                bulletCount: bulletCount
            })
        });

        const data = await response.json();
        document.getElementById("output-notes").innerText = data.summary;
    } catch (e) {
        document.getElementById("output-notes").innerText =
            "⚠️ Error generating notes. Please try again later.";
        console.error(e);
    }
});


